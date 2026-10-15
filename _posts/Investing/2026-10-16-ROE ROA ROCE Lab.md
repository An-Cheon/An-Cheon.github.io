---
layout: post
title:  回报率拖拽实验室：ROE · ROA · ROCE
categories: [Others, Investing]
tags: [investing, finance]
---

拖动资产负债表和利润表里的方块，看 ROE、ROA、ROCE 怎么跟着变。[全屏打开](/assets/html/roe-roa-roce.html){:target="_blank"}

<!-- more -->

<iframe id="ratio-lab" src="/assets/html/roe-roa-roce.html" title="回报率拖拽实验室" style="display:block;width:100%;height:1600px;border:0;border-radius:8px;"></iframe>
<script>
(function () {
  var frame = document.getElementById('ratio-lab');
  var root = document.documentElement;
  function doc() { try { return frame.contentDocument; } catch (e) { return null; } }
  /* Chirpy puts the light/dark mode on html[data-bs-theme] (older versions: data-mode); the lab reads html[data-theme]. */
  function syncTheme() {
    var d = doc();
    if (!d) return;
    var mode = root.getAttribute('data-bs-theme') || root.getAttribute('data-mode');
    if (mode) d.documentElement.setAttribute('data-theme', mode);
    else d.documentElement.removeAttribute('data-theme');
  }
  function fit() {
    var d = doc();
    /* body height, not documentElement.scrollHeight: the latter never drops below the frame's own height. */
    if (d && d.body) frame.style.height = Math.ceil(d.body.getBoundingClientRect().height) + 'px';
  }
  function init() {
    var d = doc();
    if (!d || d.URL === 'about:blank') return;
    syncTheme();
    fit();
    if (window.ResizeObserver) new ResizeObserver(fit).observe(d.body);
  }
  frame.addEventListener('load', init);
  /* A cached frame can finish loading before this script runs. */
  if (doc() && doc().readyState === 'complete') init();
  new MutationObserver(syncTheme).observe(root, { attributes: true, attributeFilter: ['data-bs-theme', 'data-mode'] });
})();
</script>
