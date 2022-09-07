---
layout: post
title: Git初始化配置以及配置github
---
<!-- more -->
git config --global user.name "这里换上你的用户名"                      

git config --global user.email "这里换上你的邮箱"                   

ssh-keygen -t rsa -C "这里换上你的邮箱"                

将id_rsa.pub拷贝放到github远程仓库中ssh中               
 
ssh -T git@github.com              

yes                 

如果配置成功会出现Hi