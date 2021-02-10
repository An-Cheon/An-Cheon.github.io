---
layout: post
title: 天天向上的力量
---
<!-- more -->
## 持续的价值   
### 1‰的力量 
一年365天，每天进步1‰    
一年365天，每天退步1‰    
```python
dayup = pow(1.001, 365)
daydown = pow(0.999, 365)
print("向上：{:.2f}，向下：{:.2f}".format(dayup, daydown))
``` 
结果:       
```shell
向上：1.44，向下：0.69
```
1‰的力量，接近2倍，不可小觑哦   

### 5‰和1%的力量    
```python
dayfactor = 0.005
dayup = pow(1+dayfactor, 365)
daydown = pow(1-dayfactor, 365)
print("向上：{:.2f}，向下：{:.2f}".format(dayup, daydown))
``` 
结果:    
```shell
向上：6.17，向下：0.16
```
5‰的力量，惊讶！    
   
```python
dayfactor = 0.01
dayup = pow(1+dayfactor, 365)
daydown = pow(1-dayfactor, 365)
print("向上：{:.2f}，向下：{:.2f}".format(dayup, daydown))
```
结果:    
```shell
向上：37.78，向下：0.03
```
1%的力量，惊人！     

### 工作日的力量    
一年365天，一周5个工作日，每天进步1%     
一年365天，一周2个休息日，每天退步1%      
```python
dayup = 1.0
dayfactor = 0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup*(1-dayfactor)
    else:
        dayup = dayup*(1+dayfactor)
print("工作日的力量：{:.2f} ".format(dayup))
```
结果:    
```shell
工作日的力量：4.63 
```
尽管工作日提高1%，但总体效果介于1‰和5‰的力量之间      

### 工作日的努力    
工作日模式要努力到什么水平，才能与每天努力1%一样？    
A君: 一年365天，每天进步1%，不停歇     
B君: 一年365天，每周工作5天休息2天，休息日下降1%，要多努力呢？     
```python
def dayUP(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup*(1 - 0.01)
        else:
            dayup = dayup*(1 + df)
    return dayup
dayfactor = 0.01
while dayUP(dayfactor) < 37.78:
    dayfactor += 0.001
print("工作日的努力参数是：{:.3f} ".format(dayfactor))
```
结果:    
```shell
工作日的努力参数是：0.019 
```
工作日模式，每天要努力到1.9%，相当于365模式每天1%的效果！     
- GRIT，坚毅，对长期目标的持续激情及持久耐力         
- GRIT是获得成功最重要的因素之一，牢记天天向上的力量        

整理自北京理工大学 《Python语言程序设计》,嵩天、黄天羽、礼欣
