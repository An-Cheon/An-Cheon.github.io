---
layout: page
title: Search
icon: fas fa-search
order: 5
---

<link href="/pagefind/pagefind-ui.css" rel="stylesheet" />

<div id="pagefind-search"></div>

<script src="/pagefind/pagefind-ui.js"></script>
<script>
  window.addEventListener("DOMContentLoaded", function () {
    // The index is built with `--force-language zh`, so it is keyed as the
    // Chinese index. The site UI is English (<html lang="en">), so point
    // Pagefind at the Chinese index explicitly before initialising the UI.
    document.documentElement.lang = "zh";
    new PagefindUI({
      element: "#pagefind-search",
      showSubResults: true,
      showImages: false,
      excerptLength: 30
    });
  });
</script>
