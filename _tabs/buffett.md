---
layout: page
title: Buffett Letters
icon: fas fa-envelope-open-text
order: 6
---

{% assign letters = site.posts | where_exp: "p", "p.letter_type" %}
{% assign partnership = letters | where: "letter_type", "partnership" | sort: "date" %}
{% assign berkshire = letters | where: "letter_type", "berkshire" | sort: "letter_year" %}
{% assign special = letters | where: "letter_type", "special" | sort: "date" %}

<style>
  .bl-intro { color: var(--text-muted-color); margin-bottom: 1.5rem; }
  .bl-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(9.5rem, 1fr)); gap: .5rem; margin: .75rem 0 1.75rem; padding: 0; list-style: none; }
  .bl-grid.bl-wide { grid-template-columns: repeat(auto-fill, minmax(15rem, 1fr)); }
  .bl-grid li { margin: 0; }
  .bl-grid a { display: block; padding: .55rem .75rem; border: 1px solid var(--main-border-color); border-radius: .5rem; background: var(--card-bg); color: var(--text-color); text-decoration: none; border-bottom: 1px solid var(--main-border-color); line-height: 1.35; transition: border-color .15s, color .15s; }
  .bl-grid a:hover { border-color: var(--link-color); color: var(--link-color); }
  .bl-grid small { display: block; color: var(--text-muted-color); font-size: .75rem; margin-top: .15rem; }
</style>

<p class="bl-intro">共收录 {{ letters.size }} 篇：合伙人信 {{ partnership.size }} 篇、伯克希尔股东信 {{ berkshire.size }} 篇、特别信件 {{ special.size }} 篇。只收原文译文，不含概括。</p>

<h2 id="partnership">合伙人时期（1956–1970）</h2>
<ul class="bl-grid">
{% for p in partnership %}<li><a href="{{ p.url | relative_url }}">{{ p.title | remove: " 巴菲特致合伙人信" }}<small>{{ p.date | date: "%Y-%m-%d" }}</small></a></li>
{% endfor %}</ul>

<h2 id="berkshire">伯克希尔时期（{{ berkshire.first.letter_year }}–{{ berkshire.last.letter_year }}）</h2>
{% assign decades = berkshire | group_by_exp: "p", "p.letter_year | divided_by: 10" %}
{% for d in decades %}
<h3 id="decade-{{ d.name }}0">{{ d.name }}0 年代</h3>
<ul class="bl-grid">
{% for p in d.items %}<li><a href="{{ p.url | relative_url }}">{{ p.letter_year }} 股东信<small>{{ p.date | date: "%Y-%m-%d" }} 发出</small></a></li>
{% endfor %}</ul>
{% endfor %}

<h2 id="special">特别信件</h2>
<ul class="bl-grid bl-wide">
{% for p in special %}<li><a href="{{ p.url | relative_url }}">{{ p.title }}<small>{{ p.date | date: "%Y-%m-%d" }}</small></a></li>
{% endfor %}</ul>
