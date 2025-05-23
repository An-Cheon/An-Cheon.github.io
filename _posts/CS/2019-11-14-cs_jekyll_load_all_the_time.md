---
layout: post
title: jekyll context is loading all the time
categories: [CS, Jekyll]
tags: [jekyll]
---
<!-- more -->
To solve this problem,I used Wireshark to analyse.       
And then:       
```shell
85	2.155418	172.20.124.1	202.118.224.101	DNS	78	Standard query 0x7e86 AAAA ancheon.disqus.com
86	2.182106	172.20.124.1	202.118.224.100	DNS	78	Standard query 0x7e86 AAAA ancheon.disqus.com
89	2.327191	202.118.224.101	172.20.124.1	DNS	78	Standard query response 0x7e86 Server failure AAAA ancheon.disqus.com
90	2.330875	172.20.124.1	202.118.224.100	DNS	78	Standard query 0x7e86 AAAA ancheon.disqus.com
98	2.500773	202.118.224.100	172.20.124.1	DNS	78	Standard query response 0x7e86 Server failure AAAA ancheon.disqus.com
```      
I searched 'disqus' in my github repo to know what it is       
An I found:   

_includes/disqus.html       
```shell
 if site.disqus 
 ......
```       
_config.yml
```shell
  googleplus: # anything in your profile username that comes after plus.google.com/
# Enter your Disqus shortname (not your username) to enable commenting on posts
# You can find your shortname on the Settings page of your Disqus account
disqus: Ancheon
```      
_layouts/post.html
```shell
   include disqus.html
   ......
```      
So, delete _includes/disqus.html and delete disqus in _config.yml and _layouts/post.html.      
You're done ! ! !
