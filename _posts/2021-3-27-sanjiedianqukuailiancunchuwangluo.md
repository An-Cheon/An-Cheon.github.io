---
layout: post
title: 3个节点的区块链存储网络
categories: [CS, PYTHON]
tags: [python]
---
<!-- more -->
开发环境：win10，python 3.7.4，Flask==1.1.0，requests==2.22             
项目地址：[link](https://github.com/An-Cheon/a_blockchain_network_1.0)           
                         
使用方法:            
1. 
   ```
   pip install -r requirements.txt             
   ```
2. 运行 CMD.py         
3. 运行任意一个run_app.py即可                  
4. 命令行中输入             
   ```
   curl -X GET http://localhost:8000/chain               
   curl -X GET http://localhost:8001/chain                  
   curl -X GET http://localhost:8002/chain            
   ```     
   显示各节点存储的区块链信息
5. 命令行中输入           
   ```
   curl -X POST http://127.0.0.1:8001/register_with -H "Content-Type:application/json" -d "{\"node_address\": \"http://127.0.0.1:8000\"}"                            
   ``` 
   建立连接
                 
说明：                     
提交信息后信息并不会显示在网页上，挖矿之后信息才会被存储在区块链中，信息现实在网页上             
在该模型中运行了run_app的节点才可以挖矿，剩下的节点只是记录信息             
