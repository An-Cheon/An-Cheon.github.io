---
layout: post
title: 消除笔记本电啸声
categories: [CS, Windows]
tags: [windows]
---
<!-- more -->
方法：关闭intel的节能技术，声音来源于CPU变频引起的电容啸叫            

步骤：          

1、管理员命令行运行：reg add HKLM\System\CurrentControlSet\Control\Processor /v Capabilities /t REG_DWORD /d 0x0007e066           

2、重启电脑          

恢复上述操作之前状态的步骤：          

1、管理员命令行运行：reg delete HKLM\System\CurrentControlSet\Control\Processor /v Capabilities /f           

2、重启电脑          
