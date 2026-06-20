#!/usr/bin/env ruby
#
# Set `last_modified_at` on posts from git history.
#
# The previous version shelled out to git once (sometimes twice) *per post*,
# spawning ~1 process for every file in `_posts`. With hundreds of posts that
# dominated the build time (each `git` spawn is ~0.2s, so it scaled linearly
# into minutes). This version makes a single `git log` pass over the whole
# history and looks each post up in the result.

Jekyll::Hooks.register :site, :post_read do |site|
  # One pass, newest commit first. `core.quotepath=false` keeps non-ASCII
  # paths (e.g. Chinese filenames) un-escaped so they match Jekyll's
  # `relative_path`; `--no-renames` keeps each commit as a plain A/M/D entry.
  log = `git -c core.quotepath=false log --name-status --no-renames --pretty=format:"commit %ad" --date=iso 2>/dev/null`
  next if log.nil? || log.empty?

  last_date = {}            # path => most recent commit date (ISO string)
  commits   = Hash.new(0)   # path => number of commits touching it
  current   = nil

  log.each_line do |line|
    line.chomp!
    if line.start_with?("commit ")
      current = line[7..-1]
    elsif line =~ /\A[AMD]\t(.+)\z/
      path = $1
      last_date[path] ||= current   # first occurrence == newest commit
      commits[path]  += 1
    end
  end

  site.posts.docs.each do |post|
    rel = post.relative_path
    # Only treat a post as "modified" when more than one commit touched it,
    # matching the old `git rev-list --count > 1` behaviour.
    next unless commits[rel] > 1
    post.data["last_modified_at"] = last_date[rel]
  end
end
