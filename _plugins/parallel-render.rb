# frozen_string_literal: true
#
# Multi-process rendering for `jekyll build`.
#
# Jekyll renders every document and page one after another in a single Ruby
# thread (and Ruby threads cannot run Liquid in parallel because of the GVL),
# so on CI one CPU core does all the work while the others sit idle. This
# plugin forks worker processes that each render a contiguous slice of the
# site and pipe the finished HTML back to the parent, which then writes
# everything exactly as Jekyll normally would.
#
# The output must be byte-for-byte identical to a serial build, so the plugin
# reproduces the two pieces of cross-document state that make Jekyll's serial
# output order-dependent:
#
#   1. `doc.content` of OTHER documents. Jekyll overwrites a document's
#      content with its converted HTML when that document is rendered, and
#      Chirpy's related-posts / home cards read other posts' `post.content`.
#      So while item i is rendered, items before it hold converted HTML and
#      items after it still hold their raw source. Phase 1 (serial, cheap:
#      Markdown output is in .jekyll-cache) converts every item's content in
#      order; each worker then restores exactly the serial state for every
#      item it renders.
#   2. Liquid `assign`s that persist inside cached layout templates between
#      renders. Each worker first re-renders the item just before its slice
#      (output discarded) so the templates carry the same leftovers as in a
#      serial build.
#
# Enabled only when JEKYLL_RENDER_WORKERS is set (a number, or "auto" for one
# worker per CPU) on a platform with fork(2) — i.e. in the GitHub Actions
# build. Local `jekyll serve` / Windows keep Jekyll's normal serial render.

require "etc"

module ParallelRender
  def render
    workers = ParallelRender.worker_count
    return super if workers < 2 || config["profile"]

    relative_permalinks_are_deprecated
    payload = site_payload
    Jekyll::Hooks.trigger :site, :pre_render, self, payload

    # Same items, same order as Site#render_docs followed by Site#render_pages.
    items = []
    collections.each_value { |c| c.docs.each { |d| items << d } }
    pages.each { |p| items << p }
    items.select! { |item| regenerator.regenerate?(item) }

    started = Process.clock_gettime(Process::CLOCK_MONOTONIC)
    raw = items.map(&:content)
    items.each { |item| ParallelRender.convert_content(item, payload) }
    converted = items.map(&:content)
    phase1 = Process.clock_gettime(Process::CLOCK_MONOTONIC) - started

    outputs = ParallelRender.render_layouts_in_workers(items, raw, converted, payload, workers)

    items.each_with_index do |item, i|
      item.output = outputs.fetch(i)
      item.trigger_hooks(:post_render)
    end

    total = Process.clock_gettime(Process::CLOCK_MONOTONIC) - started
    Jekyll.logger.info "Parallel render:",
                       format("%d items, %d workers, convert %.1fs, total %.1fs",
                              items.size, workers, phase1, total)

    Jekyll::Hooks.trigger :site, :post_render, self, payload
    nil
  end

  class << self
    def worker_count
      value = ENV["JEKYLL_RENDER_WORKERS"].to_s.strip
      return 1 if value.empty? || !Process.respond_to?(:fork)

      value == "auto" ? Etc.nprocessors : value.to_i
    end

    # The first half of Jekyll::Renderer#run / #render_document: everything up
    # to (but not including) placing the content in its layouts.
    def convert_content(item, payload)
      renderer = item.renderer
      site = renderer.site
      renderer.payload = payload
      renderer.send(:assign_pages!)
      renderer.send(:assign_current_document!)
      renderer.send(:assign_highlighter_options!)
      renderer.send(:assign_layout_data!)
      item.trigger_hooks(:pre_render, payload)

      output = item.content
      if item.render_with_liquid?
        output = renderer.render_liquid(output, payload, info_for(site, payload), item.path)
      end
      item.content = renderer.convert(output.to_s)
      item.trigger_hooks(:post_convert)

      # place_in_layouts leaves payload["layout"] holding the merged data of
      # the layout chain; the next item's assign_layout_data! merges into it.
      emulate_layout_payload(item, site, payload)
    end

    def info_for(site, payload)
      liquid = site.config["liquid"] || {}
      {
        :registers        => { :site => site, :page => payload["page"] },
        :strict_filters   => liquid["strict_filters"],
        :strict_variables => liquid["strict_variables"],
      }
    end

    def emulate_layout_payload(item, site, payload)
      return unless item.place_in_layout?

      layout = site.layouts[item.data["layout"].to_s]
      payload["layout"] = nil
      used = Set.new([layout])
      while layout
        payload["layout"] = Jekyll::Utils.deep_merge_hashes(layout.data, payload["layout"] || {})
        layout = site.layouts[layout.data["layout"]]
        break if layout.nil? || used.include?(layout)

        used << layout
      end
    end

    # The second half of Jekyll::Renderer#run: wrap already-converted content
    # in its layouts.
    def render_layout(item, payload)
      renderer = item.renderer
      renderer.payload = payload
      renderer.send(:assign_pages!)
      renderer.send(:assign_current_document!)
      renderer.send(:assign_highlighter_options!)
      return item.content unless item.place_in_layout?

      renderer.place_in_layouts(item.content, payload, info_for(renderer.site, payload))
    end

    # Splits the items into more slices than workers (the heavy listing pages
    # all sit at the end) and keeps `workers` forked processes busy.
    def render_layouts_in_workers(items, raw, converted, payload, workers)
      size = (items.size / (workers * 4).to_f).ceil
      queue = (0...items.size).each_slice(size).to_a
      Process.warmup if Process.respond_to?(:warmup)

      running = {}
      outputs = {}
      until queue.empty? && running.empty?
        running.store(*spawn_worker(items, raw, converted, payload, queue.shift)) while running.size < workers && !queue.empty?

        pid = Process.wait
        status = $?
        next unless running.key?(pid)

        result = running.delete(pid).value
        result = [:error, "worker #{pid} exited with #{status.inspect}", []] if result.nil?
        if result.first == :error
          running.each_key { |p| Process.kill("KILL", p) rescue nil } # rubocop:disable Style/RescueModifier
          Jekyll.logger.error "Parallel render:", result[1]
          Array(result[2]).first(15).each { |line| Jekyll.logger.error "", line }
          raise "Parallel render worker failed: #{result[1]}"
        end
        outputs.merge!(result[1])
      end
      outputs
    end

    def spawn_worker(items, raw, converted, payload, slice)
      reader, writer = IO.pipe
      reader.binmode
      writer.binmode
      pid = fork do
        reader.close
        result = begin
          [:ok, render_slice(items, raw, converted, payload, slice)]
        rescue Exception => e # rubocop:disable Lint/RescueException
          [:error, "#{e.class}: #{e.message}", e.backtrace]
        end
        writer.write(Marshal.dump(result))
        writer.close
        $stdout.flush
        $stderr.flush
        exit!(result.first == :ok ? 0 : 1)
      end
      writer.close
      # Drain the pipe in a thread so the worker never blocks on a full pipe.
      [pid, Thread.new { data = reader.read; reader.close; data.empty? ? nil : Marshal.load(data) }]
    end

    # Runs in a forked worker. Starts from the parent's post-phase-1 state
    # (every item converted) and rewinds items after the slice to raw source.
    def render_slice(items, raw, converted, payload, slice)
      Jekyll::Cache.prepend(AtomicCacheDump)

      first = slice.first
      start = [first - 1, 0].max
      (start + 1...items.size).each { |j| items[j].content = raw[j] }

      # Warm-up: re-render the item before this slice so cached layout
      # templates hold the same leftover assigns as in a serial build.
      render_layout(items[start], payload) if first.positive?

      slice.each_with_object({}) do |i, out|
        items[i].content = converted[i]
        out[i] = render_layout(items[i], payload)
      end
    end
  end

  # Workers share .jekyll-cache; write cache files atomically so a worker
  # never reads another worker's half-written entry.
  module AtomicCacheDump
    def dump(path, value)
      return unless disk_cache_enabled?

      FileUtils.mkdir_p(File.dirname(path))
      tmp = "#{path}.#{Process.pid}.tmp"
      File.open(tmp, "wb") { |f| Marshal.dump(value, f) }
      File.rename(tmp, path)
    end
  end
end

Jekyll::Site.prepend(ParallelRender)
