---
layout: post
title: C++ 所有断点都不命中，并且c++程序生成的exe程序一直维持高cpu占用。
categories: [CS, C++]
tags: [c++]
---

可能是某个数据初始化时有死循环，例如结构体中的构造。所以一直无法进入main函数。
