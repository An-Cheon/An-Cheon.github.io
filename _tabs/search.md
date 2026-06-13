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
  /* Hide the "↳ heading" sub-result line; keep only the matching sentence */
  #pagefind-search .pagefind-ui__result-nested .pagefind-ui__result-link {
    display: none;
  }
  /* The matching sentence reads like text but is clickable (jumps to the term) */
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
  window.addEventListener("DOMContentLoaded", function () {
    document.documentElement.lang = "zh";
    new PagefindUI({
      element: "#pagefind-search",
      language: "zh",
      showSubResults: true,
      showImages: false,
      excerptLength: 30,
      pageSize: 1000,
      processTerm: function (term) {
        term = term.trim();
        if (!term) return term;
        return '"' + term.replace(/^"+|"+$/g, "") + '"';
      },
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
    var hasSeg = typeof Intl !== "undefined" && !!Intl.Segmenter;
    var segOut = "n/a";
    if (hasSeg) {
      try {
        var s = new Intl.Segmenter("zh", { granularity: "word" });
        var arr = [];
        var it = s.segment("中国股市");
        for (var p of it) { arr.push(p.segment); }
        segOut = arr.join("|");
      } catch (e) { segOut = "err:" + e.message; }
    }
    diag.textContent = "DIAG | Segmenter=" + hasSeg + " | seg(中国股市)=[" + segOut + "]";
    root.appendChild(diag);
  });
</script>
