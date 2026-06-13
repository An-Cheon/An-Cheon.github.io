---
layout: page
title: Search
icon: fas fa-search
order: 5
---

<style>
  #cs-wrap { position: relative; margin-bottom: .25rem; }
  #cs-input {
    width: 100%;
    padding: .6rem 1rem .6rem 2.4rem;
    font-size: 1rem;
    color: var(--text-color);
    background: var(--main-bg);
    border: 1px solid var(--main-border-color);
    border-radius: 1.5rem;
    outline: none;
    box-sizing: border-box;
  }
  #cs-input:focus { border-color: var(--link-color); }
  #cs-icon { position: absolute; left: .95rem; top: 50%; transform: translateY(-50%); color: var(--text-muted-color); }
  #cs-status { color: var(--text-muted-color); font-size: .9rem; margin: .9rem 0; }
  .cs-result { padding: 1rem 0; border-top: 1px solid var(--main-border-color); }
  .cs-title { font-size: 1.1rem; font-weight: 700; margin-bottom: .15rem; }
  .cs-title a { color: var(--heading-color); text-decoration: none; }
  .cs-title a:hover { text-decoration: underline; }
  .cs-sentence { display: block; margin-top: .45rem; color: var(--text-muted-color); line-height: 1.7; text-decoration: none; }
  .cs-sentence:hover { text-decoration: underline; }
  .cs-sentence mark { background: transparent; color: var(--link-color); font-weight: 700; padding: 0; }
  #cs-diag { margin-top: 1.5rem; padding: .5rem; border: 1px dashed var(--main-border-color); font-size: .8rem; color: var(--text-muted-color); word-break: break-all; }
</style>

<div id="cs-wrap">
  <i id="cs-icon" class="fas fa-search"></i>
  <input id="cs-input" type="search" autocomplete="off" placeholder="Search..." aria-label="Search" />
</div>
<div id="cs-status"></div>
<div id="cs-results"></div>
<div id="cs-diag"></div>

<script>
  function cjkSegOk() {
    try {
      if (!(typeof Intl !== "undefined" && Intl.Segmenter)) return false;
      var parts = Array.from(new Intl.Segmenter("zh", { granularity: "word" }).segment("中国")).map(function (p) { return p.segment; });
      return parts.length === 1;
    } catch (e) { return false; }
  }
  function makeJiebaSegmenter(cut) {
    return class {
      constructor(locales, options) { this.gran = (options && options.granularity) || "grapheme"; }
      segment(input) {
        var out = [];
        if (this.gran === "word") {
          var words = cut(input, true);
          var idx = 0;
          for (var i = 0; i < words.length; i++) {
            out.push({ segment: words[i], index: idx, input: input, isWordLike: true });
            idx += words[i].length;
          }
        } else {
          var j = 0;
          for (var ch of input) { out.push({ segment: ch, index: j, input: input, isWordLike: true }); j += ch.length; }
        }
        return out;
      }
    };
  }
  async function ensureSegmenter() {
    if (cjkSegOk()) return "native";
    try {
      var mod = await import("https://cdn.jsdelivr.net/npm/jieba-wasm@2.4.0/pkg/web/jieba_rs_wasm.js");
      await mod.default();
      Intl.Segmenter = makeJiebaSegmenter(mod.cut);
      return cjkSegOk() ? "jieba" : "jieba-nofix";
    } catch (e) { return "jieba-error:" + (e && e.message ? e.message : e); }
  }

  (async function () {
    var MAX_ARTICLES = 500;
    var segState = await ensureSegmenter();
    document.documentElement.lang = "zh";

    var pagefind = await import("/pagefind/pagefind.js");
    await pagefind.options({ language: "zh" });

    var inputEl = document.getElementById("cs-input");
    var statusEl = document.getElementById("cs-status");
    var resultsEl = document.getElementById("cs-results");

    function escapeHtml(s) {
      return s.replace(/[&<>"']/g, function (c) {
        return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
      });
    }
    function escapeRegex(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); }
    function highlight(text, q) {
      var re = new RegExp(escapeRegex(q), "gi");
      var out = "", last = 0, m;
      while ((m = re.exec(text)) !== null) {
        out += escapeHtml(text.slice(last, m.index)) + "<mark>" + escapeHtml(m[0]) + "</mark>";
        last = m.index + m[0].length;
        if (m.index === re.lastIndex) re.lastIndex++;
      }
      return out + escapeHtml(text.slice(last));
    }
    function splitSentences(content) {
      return content.match(/[^。！？!?；;.\n\r]+[。！？!?；;.]?/g) || [];
    }
    function textFragment(sentence) {
      var s = sentence.trim();
      if (s.length <= 60) return "#:~:text=" + encodeURIComponent(s);
      return "#:~:text=" + encodeURIComponent(s.slice(0, 25)) + "," + encodeURIComponent(s.slice(-25));
    }

    var runId = 0, timer;
    inputEl.addEventListener("input", function () {
      clearTimeout(timer);
      timer = setTimeout(run, 220);
    });

    async function run() {
      var myId = ++runId;
      var q = inputEl.value.trim();
      resultsEl.innerHTML = "";
      if (!q) { statusEl.textContent = ""; return; }
      statusEl.textContent = "Searching…";
      var ql = q.toLowerCase();

      var words;
      try {
        words = Array.from(new Intl.Segmenter("zh", { granularity: "word" }).segment(q)).map(function (p) { return p.segment; });
      } catch (e) { words = [q]; }
      words = words.map(function (w) { return w.trim(); }).filter(function (w) { return w.length > 0; });
      var uniq = [], seenW = {};
      for (var wi = 0; wi < words.length; wi++) { if (!seenW[words[wi]]) { seenW[words[wi]] = 1; uniq.push(words[wi]); } }
      if (!uniq.length) uniq = [q];

      var counts;
      try {
        counts = await Promise.all(uniq.map(async function (w) {
          try { var r = await pagefind.search(w); return { n: r.results.length, results: r.results }; }
          catch (e) { return { n: 0, results: [] }; }
        }));
      } catch (e) { statusEl.textContent = "Search error"; return; }
      if (myId !== runId) return;

      var positive = counts.filter(function (c) { return c.n > 0; });
      if (!positive.length) { statusEl.textContent = '0 results for "' + q + '"'; return; }
      positive.sort(function (a, b) { return a.n - b.n; });
      var cands = positive[0].results;
      var truncated = cands.length > MAX_ARTICLES;
      if (truncated) cands = cands.slice(0, MAX_ARTICLES);

      var datas = await Promise.all(cands.map(function (c) { return c.data(); }));
      if (myId !== runId) return;

      var html = "", count = 0;
      for (var i = 0; i < datas.length; i++) {
        var content = datas[i].content || "";
        if (content.toLowerCase().indexOf(ql) === -1) continue;
        var seen = {}, uniq = [];
        var sents = splitSentences(content);
        for (var j = 0; j < sents.length; j++) {
          var t = sents[j].trim();
          if (t && t.toLowerCase().indexOf(ql) !== -1 && !seen[t]) { seen[t] = 1; uniq.push(t); }
        }
        if (!uniq.length) continue;
        count++;
        var url = datas[i].url;
        var title = (datas[i].meta && datas[i].meta.title) ? datas[i].meta.title : url;
        var block = '<div class="cs-result"><div class="cs-title"><a href="' + url + '">' + escapeHtml(title) + "</a></div>";
        for (var k = 0; k < uniq.length; k++) {
          block += '<a class="cs-sentence" href="' + url + textFragment(uniq[k]) + '">' + highlight(uniq[k], q) + "</a>";
        }
        html += block + "</div>";
      }
      if (myId !== runId) return;
      resultsEl.innerHTML = html;
      statusEl.textContent = count + (count === 1 ? " result" : " results") + ' for "' + q + '"' + (truncated ? " (scanned first " + MAX_ARTICLES + " matches)" : "");
    }

    var diag = document.getElementById("cs-diag");
    var seg = "n/a";
    try { seg = Array.from(new Intl.Segmenter("zh", { granularity: "word" }).segment("自由市场")).map(function (p) { return p.segment; }).join("|"); } catch (e) { seg = "err"; }
    diag.textContent = "DIAG | state=" + segState + " | seg(自由市场)=[" + seg + "]";
  })();
</script>
