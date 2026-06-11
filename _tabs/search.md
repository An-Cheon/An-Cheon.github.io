---
layout: page
title: 搜索
icon: fas fa-search
order: 5
---

<link href="/pagefind/pagefind-ui.css" rel="stylesheet" />

<div id="pagefind-search"></div>

<script src="/pagefind/pagefind-ui.js"></script>
<script>
  window.addEventListener("DOMContentLoaded", function () {
    new PagefindUI({
      element: "#pagefind-search",
      showSubResults: true,
      showImages: false,
      excerptLength: 30,
      translations: {
        placeholder: "搜索全站文章…",
        clear_search: "清除",
        load_more: "加载更多结果",
        search_label: "搜索本站",
        filters_label: "筛选",
        zero_results: "没有找到与「[SEARCH_TERM]」相关的内容",
        many_results: "找到 [COUNT] 条与「[SEARCH_TERM]」相关的结果",
        one_result: "找到 [COUNT] 条与「[SEARCH_TERM]」相关的结果",
        alt_search: "未找到「[SEARCH_TERM]」，改为显示「[DIFFERENT_TERM]」的结果",
        search_suggestion: "未找到「[SEARCH_TERM]」的结果，可尝试以下搜索：",
        searching: "正在搜索「[SEARCH_TERM]」…"
      }
    });
  });
</script>
