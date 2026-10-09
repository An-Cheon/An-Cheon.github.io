---
layout: post
title: 隐藏WIN10中误显示的EFI分区(Z盘)
categories: [CS, Windows]
tags: [windows]
---
<!-- more -->
本来想着直接在命令行里操作结果却显示:
         
'diskpart' 不是内部或外部命令，也不是可运行的程序    
或批处理文件。    
![](/images/diskpart_1.png)         
可能是系统盘中该功能的路径出了问题,但是应该还是有diskpart功能的,所以在C盘中搜索diskpart.       
![](/images/diskpart_2.png)      
下面的就是找出来的正确的diskpark程序了.    
![](/images/diskpart_3.png)      
list disk      
看一下都有什么盘      
![](/images/diskpart_4.png)         
select disk 0      
选中默认磁盘0      
![](/images/diskpart_5.png)       
list volume     
查看磁盘0的分区      
![](/images/diskpart_6.png)       
select volume z      
选择想要隐藏的分区z(命令行中是小写)     
![](/images/diskpart_7.png)       
remove letter=z     
删除挂载点z      
![](/images/diskpart_8.png)       
完成!z盘隐藏成功!     
![](/images/diskpart_9.png)          
          
