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
</style>

<div id="pagefind-search"></div>

<script src="/pagefind/pagefind-ui.js"></script>
<script>
  window.addEventListener("DOMContentLoaded", function () {
    document.documentElement.lang = "zh";
    new PagefindUI({
      element: "#pagefind-search",
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
  });
</script>
