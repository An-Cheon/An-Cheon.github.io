---
layout: page
title: Search
icon: fas fa-search
order: 5
---

<link href="/pagefind/pagefind-ui.css" rel="stylesheet" />

<style>
  #pagefind-search {
    --pagefind-ui-scale: 0.9;
    --pagefind-ui-primary: var(--link-color);
    --pagefind-ui-text: var(--text-color);
    --pagefind-ui-background: var(--main-bg);
    --pagefind-ui-border: var(--main-border-color);
    --pagefind-ui-tag: var(--card-bg);
    --pagefind-ui-font: inherit;
  }
  #pagefind-search .pagefind-ui__result-title .pagefind-ui__result-link {
    color: var(--heading-color);
  }
  #pagefind-search .pagefind-ui__result-excerpt {
    color: var(--text-muted-color);
  }
  #pagefind-search mark {
    background: transparent;
    color: var(--link-color);
    font-weight: 700;
    padding: 0;
  }
  #pagefind-search .pagefind-ui__message {
    color: var(--text-muted-color);
  }
  #pagefind-search .pagefind-ui__result-nested .pagefind-ui__result-link {
    display: none;
  }
  #pagefind-search .pagefind-ui__result-excerpt a.result-jump {
    color: var(--text-muted-color);
    text-decoration: none;
  }
  #pagefind-search .pagefind-ui__result-excerpt a.result-jump:hover {
    text-decoration: underline;
  }
</style>

<div id="pagefind-search"></div>

<script src="/pagefind/pagefind-ui.js"></script>
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
    var segState = await ensureSegmenter();
    document.documentElement.lang = "zh";
    new PagefindUI({
      element: "#pagefind-search",
      language: "zh",
      showSubResults: true,
      showImages: false,
      excerptLength: 30,
      pageSize: 1000,
      translations: {
        placeholder: "Search...",
        clear_search: "Clear",
        load_more: "Load more results",
        search_label: "Search this site",
        filters_label: "Filters",
        zero_results: "No results for [SEARCH_TERM]",
        many_results: "[COUNT] results for [SEARCH_TERM]",
        one_result: "[COUNT] result for [SEARCH_TERM]",
        alt_search: "No results for [SEARCH_TERM]. Showing results for [DIFFERENT_TERM] instead",
        search_suggestion: "No results for [SEARCH_TERM]. Try one of the following searches:",
        searching: "Searching for [SEARCH_TERM]..."
      }
    });

    var root = document.getElementById("pagefind-search");
    var observer = null;
    function currentTerm() {
      var inp = root.querySelector(".pagefind-ui__search-input") || root.querySelector("input");
      return inp ? inp.value.trim().replace(/^"+|"+$/g, "") : "";
    }
    function decorate() {
      if (observer) observer.disconnect();
      var term = currentTerm();
      root.querySelectorAll(".pagefind-ui__result-nested").forEach(function (nested) {
        var excerpt = nested.querySelector(".pagefind-ui__result-excerpt");
        var link = nested.querySelector(".pagefind-ui__result-link");
        if (excerpt && link && !excerpt.querySelector("a.result-jump")) {
          var base = link.href.split("#")[0];
          var href = base + (term ? "#:~:text=" + encodeURIComponent(term) : "");
          var a = document.createElement("a");
          a.className = "result-jump";
          a.href = href;
          a.innerHTML = excerpt.innerHTML;
          excerpt.innerHTML = "";
          excerpt.appendChild(a);
        }
      });
      if (observer) observer.observe(root, { childList: true, subtree: true });
    }
    observer = new MutationObserver(decorate);
    observer.observe(root, { childList: true, subtree: true });

    var diag = document.createElement("div");
    diag.style.cssText = "margin-top:1.5rem;padding:.5rem;border:1px dashed var(--main-border-color);font-size:.8rem;color:var(--text-muted-color);word-break:break-all";
    var segOut = "n/a";
    try {
      segOut = Array.from(new Intl.Segmenter("zh", { granularity: "word" }).segment("中国共产党")).map(function (p) { return p.segment; }).join("|");
    } catch (e) { segOut = "err:" + e.message; }
    var api = "n/a";
    try {
      var pf = await import("/pagefind/pagefind.js?cb=" + Date.now());
      await pf.options({ language: "zh" });
      var rr = await pf.search("中国共产党");
      api = (rr && rr.results) ? String(rr.results.length) : "0";
    } catch (e) { api = "err:" + (e && e.message ? e.message : e); }
    diag.textContent = "DIAG | state=" + segState + " | seg(中国共产党)=[" + segOut + "] | plain(中国共产党)=" + api;
    root.appendChild(diag);
  })();
</script>
