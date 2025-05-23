---
layout: post
title: Your site is having problems building
categories: [CS, Jekyll]
tags: [jekyll]
---
Tried many times for browsing an-cheon.com after upload a new .md file,but the website didn't change at all.<!-- more -->            
Solve : When I saw setting of GitHub Pages,I found this:
     
Your site is having problems building: The variable 2{2,3,0} on line 17 in _posts/2019-10-7-8 puzzle 4 ways to solve with java.md was not properly closed with }}. For more information, see https://help.github.com/en/articles/troubleshooting-jekyll-build-errors-for-github-pages-sites#tag-not-properly-terminated.      (2{means {and{,but I can't write down this syntax error at here.......)

It means I failed in built my changed website.After solved these problems,it worked.      
It teach me that after pushed new change,I should ckek that the website is built or not.

 
