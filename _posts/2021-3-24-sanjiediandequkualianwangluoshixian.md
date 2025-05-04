---
layout: post
title: 3个节点的区块链网络的实现
---
#### &#8195;从单个节点开始构建区块链网络              
#### &#8195;已实现的3节点区块链网络         
<!-- more -->
### 1.基本使用方式               
原项目文件备份地址：https://github.com/An-Cheon/a_blockchain_nerwork/blob/master/blockchain-python-master.zip        
#### 使用方法：                        
使用指导：

- 创建账户
```
$ python console account create
```
- 开始挖矿
```
$ python console miner start 3008
```
- 转账交易
```
$ python console tx transfer from_address to_address amount
```
- 交易记录
```
$ python console tx list
```
- 查看所有区块
```
$ python console blockchain list
```

### 节点网络

复制源码到一个新的目录，作为新的节点.或者复制到另一台机器上。下面代码演示本机两个节点：
- 启动新节点   
```
$ cd {another_blockchain_directory}
$ python console node add 127.0.0.1:3008
$ python console node run 3009
```
- 回到初始的源码目录下，要保证挖矿正在进行当中，然后添加新的节点：   
```
$ python console node add 127.0.0.1:3009
```
当一个新的区块块被挖掘时，新的区块和交易将广播给其他节点。
多个节点情况下，只要一个节点被添加，所有节点网络会同步。

## 命令行大全
使用如下:   
```
$ python console [module] [action] params...
```
比如:
```
$ python console tx list
```

更详细的说明在压缩文件中的说明表格中                 
                               

### 2.三节点区块链网络使用方式                                   
3节点网络地址https://github.com/An-Cheon/a_blockchain_nerwork                
该网络使用方法：                    
在3008目录中：               
```
$ python console miner start 3008
```
在3009目录中：               
```
$ python console miner start 3009
```
在3010目录中：               
```
$ python console miner start 3010
```

