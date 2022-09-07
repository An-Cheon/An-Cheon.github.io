---
layout: post
title: 华为机试
---
<!-- more -->
HJ1 字符串最后一个单词的长度                    

```python
a = input()
b = a.split(" ")
print(len(b[len(b) - 1]))
```

HJ2 计算某字符出现次数                 

```python
a = input().lower()
b = input().lower()
print(a.count(b))
```

HJ3 明明的随机数       

```python
a = int(input())
b = []
for i in range(a):
    temp = int(input())
    b.append(temp)
c = list(set(b))
c.sort()
for i in range(len(c)):
    print(c[i])
```

HJ4 字符串分隔               

```python
a = input()
b = len(a) // 8
c = len(a) % 8
for i in range(b):
    print(a[i * 8:i* 8 + 8])
if c != 0:
    temp = a[b * 8:b * 8 + c + 1]
    for i in range(8 - c):
        temp = temp + "0"
    print(temp)
```

HJ5 进制转换              

```python
a = input()
ending = 0 
base = 1
for i in range(len(a)):
    if a[len(a) - 1 - i] == 'A':
        ending = ending + base * 10
    if a[len(a) - 1 - i] == 'B':
        ending = ending + base * 11
    if a[len(a) - 1 - i] == 'C':
        ending = ending + base * 12
    if a[len(a) - 1 - i] == 'D':
        ending = ending + base * 13
    if a[len(a) - 1 - i] == 'E':
        ending = ending + base * 14
    if a[len(a) - 1 - i] == 'F':
        ending = ending + base * 15
    if a[len(a) - 1 - i].isdigit():
        ending = ending + base * int(a[len(a) - 1 - i])
    base = base * 16
print(ending)
```

HJ6 质数因子                 


```python
import math
a = int(input())
ending = ''
for i in range(2,int(math.sqrt(a)) + 1):
    while a % i == 0:
        ending = ending + str(i) + ' '
        a = a // i
if a > 2:
    print(ending + str(a))
else:
    print(ending)
```

HJ7 取近似值               

```python
a = float(input())
if a < 1:
    if a >= 0.5:
        print(1)
    else:
        print(0)
else:
    if a / int(a) == 1:
        print(int(a))
    else:
        if a - int(a) >= 0.5:
            print(int(a) + 1)
        else:
            print(int(a))
```

HJ8 合并表记录             

```python
a = int(input())
dic = {}
temp = {}
for i in range(a):
    b = input()
    if int(b.split(" ")[0]) in dic.keys():
        dic[int(b.split(" ")[0])] =  dic[int(b.split(" ")[0])] + int(b.split(" ")[1])
    else:
        dic[int(b.split(" ")[0])] = int(b.split(" ")[1])
l = sorted(dic.keys())        
for i in range(len(l)):
    print(str(l[i]) + " " + str(dic[l[i]]))
```

HJ9 提取不重复的整数               

```python
a = int(input())
ending = ''
nums = []
if a < 10:
    print(a)
else:
    for i in range(len(str(a))):
        if str(a)[len(str(a)) - i - 1] not in nums:
            ending = ending + str(a)[len(str(a)) - i - 1]
            nums.append(str(a)[len(str(a)) - i - 1])
    print(ending)
```

HJ10 字符个数统计              

```python
a = input()
l = []
for i in range(len(a)):
    if (a[i] not in l) and  ord(a[i]) <= 127 and ord(a[i]) >=0:
        l.append(a[i])
print(len(l))
```

HJ11 数字颠倒                

```python
a = input()
ending = ''
for i in range(len(a)):
    ending = ending + a[len(a) - i - 1]
print(ending)
```

HJ12 字符串反转       

```python
a = input()
ending = ''
for i in range(len(a)):
    ending = ending + a[len(a) - i - 1]
print(ending)
```

HJ13 句子逆序              

```python
a = input()
ending = ''
if ' ' not in a:
    print(a)
else:
    for i in range(len(a.split(' '))):
        ending = ending + a.split(' ')[len(a.split(' ')) - i - 1] + ' '
    print(ending)
```

HJ14 字符串排序          

```python
a = input()
l = []
for i in range(int(a)):
    l.append(input())
l.sort()
for i in range(len(l)):
    print(l[i])
```

HJ15 求int型正整数在内存中存储时1的个数              

```python
a = int(input())
ending = 0
for i in range(a):
    if a == 0:
        break
    if a % 2 == 1:
        ending = ending + 1
    a = a // 2
print(ending)
```

HJ17 坐标移动             

```python
a = input()
l1 = a.split(';')
l2 = [] 
ending = [0,0]
for i in range(len(l1)):
    if (l1[i] != 0) and (l1[i][0:1] == 'A' or 'S' or 'W' or 'D') and l1[i][1:len(l1[i])].isdigit():
        l2.append(l1[i])
for i in range(len(l2)):
    if l2[i][0] == 'A':
        ending[0] = ending[0] - int(l2[i][1:len(l2[i])])
    if l2[i][0] == 'D':
        ending[0] = ending[0] + int(l2[i][1:len(l2[i])])
    if l2[i][0] == 'W':
        ending[1] = ending[1] + int(l2[i][1:len(l2[i])])
    if l2[i][0] == 'S':
        ending[1] = ending[1] - int(l2[i][1:len(l2[i])])
print(str(ending[0]) + ',' + str(ending[1]))
```

HJ19 简单错误记录         

```python
l = []
while True:
    try:
        a = input()
        b = a.split(' ')
        c = b[0].split('\\')
        if len(l) == 0:
            temp = c[len(c) - 1]
            if len(temp) > 16:
                l.append([temp[len(temp) - 16:len(temp)], b[1], 1])
            else:
                l.append([temp, b[1], 1])
        else:
            temp = c[len(c) - 1]
            
            if len(temp) > 16:
                d = temp[len(temp) - 16:len(temp)]
            else:
                d = c[len(c) - 1]
            flag = 0
            for i in range(len(l)):
                if l[i][0] == d and l[i][1] == b[1]:
                    l[i][2] = l[i][2] + 1
                    flag = 1
            if flag == 0:
                l.append([d, b[1], 1])
    except:
        break
if len(l) <= 8:
    for i in range(len(l)):
        print(l[i][0] + ' ' + l[i][1] + ' ' + str(l[i][2]))
else:
    n = len(l)
    for i in range(8):
        print(l[n - 8 + i][0] + ' ' + l[n - 8 + i][1] + ' ' + str(l[n - 8 + i][2]))
```

HJ20 密码验证合格程序                

```python
#不能有长度大于2的包含公共元素的子串重复，即长度大于等于3的重复
ending = []
while True:
    try:
        a = input()
        if len(a) <= 8:
            ending.append('NG')
        else:
            flag = 0
            for i in range(len(a) - 6):
                if (a[i:i + 3] in a[0:i + 1]) or (a[i:i + 3] in a[i + 2:len(a)]):
                    ending.append('NG')
                    flag = 1
                    break
            l = [0,0,0,0] #小写，大写，数字，特殊符号
            if flag == 0:
                for i in range(len(a)):
                    temp = 0
                    if a[i].islower():
                        l[0] = 1
                        temp = 1
                    if a[i].isupper():
                        l[1] = 1
                        temp = 1
                    if a[i].isdigit():
                        l[2] = 1
                        temp = 1
                    if temp == 0:
                        l[3] = 1
                if l[0] + l[1] + l[2] + l[3] < 3:
                    ending.append('NG')
                else:
                    ending.append('OK')
    except:
        break
for i in range(len(ending)):
    print(ending[i])
```

HJ21 简单密码               

```python
a = input()
ending = ''
alphabet = 'abc2def3ghi4jkl5mno6pqrs7tuv8wxyz9'
for i in range(len(a)):
    temp = 0
    if a[i].isupper():
        for j in range(len(alphabet)):
            if a[i].lower()== alphabet[j] and a[i] != 'Z':
                if alphabet[j + 1].isdigit():
                    temp = 1
                    ending = ending + alphabet[j + 2]
                else:
                    temp = 1
                    ending = ending + alphabet[j + 1]
                break
            if a[i] == 'Z':
                temp = 1
                ending = ending + 'a'
                break
    if a[i].islower():
        flag = 0
        for j in range(len(alphabet)):
            if flag == 1 and alphabet[j].isdigit():
                temp = 1
                ending = ending + alphabet[j]
                break
            if a[i] == alphabet[j]:
                flag = 1
    if temp == 0:
        ending = ending + a[i]
print(ending)
```

HJ22 汽水瓶          

```python
ending = []
def function(n):
    if n == 2:
        return 1
    if n == (0 or 1):
        return 0
    return n // 3 + function(n // 3 + n % 3)
    
while True:
    try:
        a = input()
        ending.append(function(int(a)))
    except:
        break
for i in range(len(ending)):
    print(ending[i])
```

HJ23 删除字符串中出现次数最少的字符                   

```python
dic = {}
a = input()
for i in range(len(a)):
    if a[i] in dic.keys():
        dic[a[i]] += 1
    else:
        dic[a[i]] = 1
temp = sorted(dic.items(), key=lambda item:item[1])
b = 0
flag = 0
for i in range(len(temp)):
    if i == 0:
        b = temp[0][1]
    else:
        if temp[0][1] == temp[i][1]:
            a = a.replace(temp[0][0], '')
            a = a.replace(temp[i][0], '')
            flag = 1
if flag == 0:
    a = a.replace(temp[0][0], '')
print(a)
```

HJ26 字符串排序

```python
def function(string, place):
    if place == 0:
        return string[1:len(string)]
    if place == len(string) - 1:
        return string[0:len(string) - 1]
    return string[0:place] + string[place + 1:len(string)]
a = input()
ending = ''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(a)):
    ending += '。'
temp = []
for i in range(len(a)):
    if (not a[i].isalpha()):
        d = list(ending)
        d[i] = a[i]
        ending = ''.join(d)
        temp.append(a[i])
for i in range(len(temp)):
    a = a.replace(temp[i], '')
temp_1 = a
for i in range(len(a)):
    min_temp = 10000
    position = -1
    for j in range(len(temp_1)):
        #print(temp_1)
        #print(j)
        if ord(temp_1[j].lower()) < min_temp:
            min_temp = ord(temp_1[j].lower())
            position = j
    for k in range(len(ending)):
        if ending[k] == '。':
            d = list(ending)
            d[k] = temp_1[position]
            ending = ''.join(d)
            break
    temp_1 = function(temp_1, position)
print(ending)
```

HJ27 查找兄弟单词                 

```python
def function(word_1,word_2):
    temp = list(word_2)
    if word_1 == word_2:
        return False
    for i in range(len(word_1)):
        for j in range(len(temp)):
            if temp[j] == word_1[i]:
                temp[j] = '。'
                break
    for i in range(len(temp)):
        if temp[i] != '。':
            return False
        if temp[i] == '。' and i == len(temp) - 1:
            return True
a = input()
b = a.split(' ')
position = int(b[len(b) - 1])
word = b[len(b) - 2]
words = []
ending = []
for i in range(len(b) - 2):
    if i != 0 and len(b[i]) == len(word):
        words.append(b[i])
for i in range(len(words)):
    if function(word,words[i]):
        ending.append(words[i])
ending = sorted(ending)
print(len(ending))
if len(ending) >= position:
    print(ending[position -1])
```

HJ29 字符串加解密                  

```python
a = input()
b = input()
alphabet1 = 'abcdefghijklmnopqrstuvwxyz'
alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ending = ['','']
for i in range(len(a)):
    if a[i].islower():
        if a[i] == 'z':
            ending[0] += 'A'
        else:
            for j in range(len(alphabet1)):
                if a[i] == alphabet1[j]:
                    ending[0] += alphabet2[j + 1]
                    break
    if a[i].isupper():
        if a[i] == 'Z':
            ending[0] += 'a'
        else:
            for j in range(len(alphabet1)):
                if a[i] == alphabet2[j]:
                    ending[0] += alphabet1[j + 1]
                    break
    if a[i].isdigit():
        if a[i] == '9':
            ending[0] += '0'
        else:
            ending[0] += str(int(a[i]) + 1)
    if (not a[i].isdigit()) and (not a[i].isalpha()):
        ending[0] += a[i]
 
for i in range(len(b)):
    if b[i].islower():
        if b[i] == 'a':
            ending[1] += 'Z'
        else:
            for j in range(len(alphabet1)):
                if b[i] == alphabet1[j]:
                    ending[1] += alphabet2[j - 1]
                    break
    if b[i].isupper():
        if b[i] == 'A':
            ending[1] += 'z'
        else:
            for j in range(len(alphabet1)):
                if b[i] == alphabet2[j]:
                    ending[1] += alphabet1[j - 1]
                    break
    if b[i].isdigit():
        if b[i] == '0':
            ending[1] += '9'
        else:
            ending[1] += str(int(b[i]) - 1)
    if (not b[i].isdigit()) and (not b[i].isalpha()):
        ending[1] += b[i]
print(ending[0])
print(ending[1])
```

HJ31 单词倒排                 

```python
a = input()
a = list(a[::-1])
ending = ''
for i in range(len(a)):
    if not a[i].isalpha():
        a[i] = ' '
start = 0
for i in range(len(a) - 1):
    flag = 0
    if a[i] != ' ' and a[i + 1] == ' ':
        flag = 1
        if start != 0:
            ending += ' '
        for j in range(i + 1 - start):
            ending += a[i - j]
    if a[i] == ' ' and a[i + 1] != ' ':
        flag = 2
        start = i + 1
    if i == len(a) - 2:
        if flag == 2:
            ending += ' '
            ending += a[i + 1]
        if flag == 0:
            if start != 0:
                ending += ' '
            for j in range(i + 2 - start):
                ending += a[i + 1 - j]
print(ending)
```

HJ33 整数与IP地址间的转换                

```python
a = input().split('.')
b = input()
temp = []
for i in range(len(a)):
    temp.append(bin(int(a[i])).replace('0b',''))
for i in range(len(temp)):
    for j in range(8 - len(temp[i])):
        temp[i] = '0' + temp[i]
temp_1 = ''
for i in range(len(temp)):
    temp_1 = temp_1 + temp[i]
temp_2 = bin(int(b)).replace('0b','')
for i in range(32-len(temp_2)):
    temp_2 = '0' + temp_2
print(int(temp_1, 2))
print(str(int(temp_2[0:8], 2)) + '.' + str(int(temp_2[8:16], 2)) + '.' + str(int(temp_2[16:24], 2)) + '.' + str(int(temp_2[24:32], 2)))
```

HJ34 图片整理                

```python
a = sorted(input())
ending = ''
for i in range(len(a)):
    ending += a[i]
print(ending)
```

HJ35 蛇形矩阵           

```python
a = int(input())
start = 1
for i in range(a):
    start = start + i
    temp = str(start)
    temp_2 = 0
    for j in range(a - i - 1):
        temp_1 = i + j + 2
        temp_2 += temp_1
        temp = temp + ' ' + str(start + temp_2)
    print(temp)
```

HJ36 字符串加密                

```python
a = list(input())
a_1 = input()
temp = []
alphabet_0 = 'abcdefghijklmnopqrstuvwxyz'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(a)):
    if not a[i] in temp:
        temp.append(a[i])
        alphabet = alphabet.replace(a[i], '')
b = ''
for i in  range(len(temp)):
    b = b + temp[i]
alphabet = b + alphabet
ending = ''
for i in range(len(a_1)):
    for j in range(len(alphabet_0)):
        if alphabet_0[j] == a_1[i]:
            ending = ending + alphabet[j]
print(ending)
```

HJ37 统计每个月兔子的总数           

```python
a = int(input())
small_rabbit = 1
middle_rabbit = 0
big_rabbit = 0
for i in range(a - 1):
    big_rabbit = big_rabbit + middle_rabbit
    middle_rabbit = small_rabbit
    small_rabbit = big_rabbit
print(small_rabbit + middle_rabbit + big_rabbit)
```

HJ38 求小球落地5次后所经历的路程和第5次反弹的高度             

```python
a = int(input())
ending = a
for i in range(4):
    ending = ending + a * (0.5 ** i)
print(ending)
print(a * (0.5 ** 5))
```

HJ40 统计字符

```python
a = input()
ending = [0,0,0,0]
for i in range(len(a)):
    flag = 0
    if a[i].isalpha():
        ending[0] = ending[0] + 1
        flag = 1
    if a[i] == ' ':
        ending[1] = ending[1] + 1
        flag = 1
    if a[i].isdigit():
        ending[2] = ending[2] + 1
        flag = 1
    if flag == 0:
        ending[3] = ending[3] + 1
for i in range(4):
    print(ending[i])
```

HJ41 称砝码           

```python
a = int(input())
b = input().split(' ')
c = input().split(' ')
weight = []
number = []
ending = [0]
for i in range(a):
    weight.append(int(b[i]))
    number.append(int(c[i]))
for i in range(number[0]):
    ending.append(weight[0] * (i + 1))
for i in range(a - 1):
    temp = list(ending)
    for j in range(len(ending)):
        for k in range(number[i + 1]):
            temp_1 = (k + 1) * weight[i + 1] + ending[j]
            if not temp_1 in ending:
                temp.append(temp_1)
    ending =list(set(temp))
print(len(ending))
```

HJ43 迷宫问题               

```python
def dfs(x,y):
    if x < 0 or y < 0 or y > int(a[1]) - 1 or x > int(a[0]) - 1 or (x,y) in used_position or graph[x][y] == '1':
        return False
    path.append('(' + str(x) + ',' + str(y) + ')')
    used_position.append((x,y))
    if (x,y) == (int(a[0]) - 1,int(a[1]) - 1) or dfs(x,y + 1) or dfs(x,y -1) or dfs(x - 1,y) or dfs(x + 1,y):
        return True
    path.pop()
path = []
used_position = []
a = input().split(' ')
graph = []
for i in range(int(a[0])):
    graph.append(input().split(' '))
dfs(0,0)
for i in range(len(path)):
    print(path[i])
```

HJ45 名字的漂亮度             

```python
a = int(input())
for i in range(a):
    b = input()
    dic = {}
    for j in range(len(b)):
        if b[j] in dic.keys():
            dic[b[j]] = dic[b[j]] + 1
        else:
            dic[b[j]] = 1
    l = []
    for temp in dic:
        l.append(dic[temp])
    l.sort()
    ending = 0
    for i in range(len(l)):
        ending = ending + l[len(l) - i - 1] * (26 - i)
    print(ending)
```

HJ46 截取字符串           

```python
a = input()
b = int(input())
print(a[0:b])
```

HJ50 四则运算            

```python
a = input()
a = a.replace('[', '(').replace(']',')').replace('{','(').replace('}',')')
print(int(eval(a)))
```

HJ53 杨辉三角的变形                     

```python
a = int(input())
if a <= 2:
    print(-1)
else:
    ending = []
    for i in range(a):
        ending.append([])
        if len(ending) == 1:
            for j in range((a - 1) * 2 + 1):
                ending[0].append(0)
            ending[0][a - 1] = 1
        else:
            temp = 0
            for j in range((a - 1) * 2 + 1):
                ending[i].append(0)
                if j == 0:
                    temp = ending[i - 1][j] + ending[i - 1][j + 1]
                else:
                    if j == (a - 1) * 2:
                        temp = ending[i - 1][j] + ending[i - 1][j - 1]
                    else:
                        temp = ending[i - 1][j - 1] + ending[i - 1][j] + ending[i - 1][j + 1]
                ending[i][j] = temp
# print(ending)
if a >= 3:
    for i in range(len(ending[0])):
        if ending[len(ending) - 1][i] % 2 == 0:
            print(i + 1)
            break
```

HJ54 表达式求值              

```python
print(eval(input()))
```

HJ55 挑7              

```python
a = int(input())
ending = 0
for i in range(a):
    if '7' in str(i + 1) or (i + 1) % 7 == 0:
        ending += 1
print(ending)
```

HJ56 完全数计算              

```python
a = int(input())
ending = []
for i in range(a):
    temp = 0
    for j in range(i):
        if (i + 1) % (j + 1) == 0:
            temp += (j + 1)
    if temp == i + 1:
        ending.append(temp)
print(len(ending))
```

HJ57 高精度整数加法

```python
a = input()
b = input()
print(eval(a + '+' + b))
```

HJ58 输入n个整数，输出其中最小的k个           

```python
a = input().split(' ')[1]
b = input().split(' ')
for i in range(len(b)):
    b[i] = int(b[i])
b.sort()
ending = ''
for i in range(int(a)):
    if i == 0:
        ending = ending + str(b[i])
    else:
        ending = ending + ' ' + str(b[i])
print(ending)
```

HJ59 找出字符串中第一个只出现一次的字符           

```python
a = input()
ending = '-1'
first = []
twice = []
for i in range(len(a)):
    if a[i] in first:
        first.remove(a[i])
        twice.append(a[i])
    if not a[i] in twice:
        first.append(a[i])
if len(first) == 0:
    print(ending)
else:
    print(first[0])
```

HJ60 查找组成一个偶数最接近的两个素数          

```python
a = int(input())
l = []
ending = [-1,-1]
gap = 10000
for i in range(1,a):
    flag = 0
    for j in range(i - 1):
        if (i + 1) % (j + 2) == 0:
            flag = 1
            break
    if flag == 0:
        l.append(i + 1)
for i in range(len(l)):
    for j in range(len(l)):
        if l[i] + l[j] == a and abs(l[i] - l[j]) < gap:
            gap = abs(l[i] - l[j])
            if i < j:
                ending[0] = l[i]
                ending[1] = l[j]
            else:
                ending[0] = l[j]
                ending[1] = l[i]
print(ending[0])
print(ending[1])
```

HJ61 放苹果              

```python
ending = []
get_input = input().split(' ')
a = int(get_input[0])
b = int(get_input[1])
def put_an_apple():
    temp = []
    for i in range(len(ending[0]) - 1):
        temp.append([])
        for j in range(len(ending[0])):
            if i == j:
                temp[i].append(ending[len(ending) - 1][j] + 1)
            else:
                if j == len(ending[0]) - 1:
                    temp[i].append(ending[len(ending) - 1][j] - 1)
                else:
                    temp[i].append(ending[len(ending) - 1][j])
        temp[i].sort()
    for i in range(len(temp)):
        if not temp[i] in ending:
            ending.append(temp[i])
            put_an_apple()
ending.append([])
for i in range(b - 1):
    ending[0].append(0)
ending[0].append(a)
put_an_apple()
print(len(ending))
```

HJ62 查找输入整数二进制中1的个数

```python
while True:
    try:
        a =  bin(int(input())).replace('0b', '')
        print(len(a.replace('0', '')))
    except:
        break
```

HJ63 DNA序列               

```python
a = input()
b = int(input())
max_cg = 0
ending = ''
for i in range(len(a) - b + 1):
    temp = 0
    for j in range(b):
        if a[i + j] in 'CG':
            temp += 1
    if temp > max_cg:
        ending = a[i:i + b]
        max_cg = temp
print(ending)
```

HJ64 MP3光标位置           

```python
a = int(input())
b = input()
show = [1, 2, 3, 4]
if a == 2:
    show = [1,2]
point = 0
for i in range(len(b)):
    if a >=4:
        if b[i] == 'U':
            if point == 0:
                if show[0] == 1:
                    show = [a - 3, a - 2, a - 1, a]
                    point = 3
                else:
                    show[0] += -1
                    show[1] += -1
                    show[2] += -1
                    show[3] += -1
            else:
                point += -1
        else:
            if point == 3:
                if show[3] == a:
                    show = [1, 2, 3, 4]
                    point = 0
                else:
                    show[0] += 1
                    show[1] += 1
                    show[2] += 1
                    show[3] += 1
            else:
                point += 1
    else:
        if a == 2:
            if b[i] == 'U':
                if point == 0:
                    point = 1
                else:
                    point += -1
            else:
                if point == 1:
                    point = 0
                else:
                    point += +1
ending = ''
for i in range(len(show)):
    if i == 0:
        ending = ending + str(show[i])
    else:
        ending = ending + ' ' + str(show[i])
print(ending)
print(show[point])
```

HJ65 查找两个字符串a,b中的最长公共子串

```python
a = input()
b = input()
enidng = ''
max_length = 0
l = []
if len(a) < len(b):
    l.append(a)
    l.append(b)
else:
    l.append(b)
    l.append(a)
for i in range(len(l[0])):
    for j in range(i + 1,len(l[0]) + 1):
        if l[0][i:j] in l[1]:
            if len(l[0][i:j]) > max_length:
                max_length = len(l[0][i:j])
                ending = l[0][i:j]
        else:
            break
print(ending)
```

HJ66 配置文件恢复                  

```python
def function(string, command):
    ending = False
    flag = 0
    if len(string) > len(command):
        return ending
    for i in range(len(string)):
        if string[i] != command[i]:
            flag = 1
    if flag == 0:
        ending = True
    return ending


while True:
    try:
        a = input()
        if not ' ' in a:
            if function(a,'reset'):
                print('reset what')
            else:
                print('unknown command')
        else:
            flag = 0
            l  = a.split(' ')
            if function(l[0],'reset') and function(l[1],'board') and (l[0] != 'r' or 're') and l[1] != 'b':
                print('board fault')
                flag = 1
            if function(l[0], 'board') and function(l[1], 'add')  and (not( (l[0] == 'b') and l[1] == 'a')):
                print('where to add')
                flag = 1
            if function(l[0], 'board') and function(l[1], 'delete'):
                print('no board at all')
                flag = 1
            if function(l[0], 'reboot') and function(l[1], 'backplane') and (l[0] != 'r' or 're') and l[1] != 'b':
                print('impossible')
                flag = 1
            if function(l[0], 'backplane') and function(l[1], 'abort') and (not( (l[0] == 'b') and l[1] == 'a')):
                print('install first')
                flag = 1
            if flag == 0:
                print('unknown command')
    except:
        break
```

HJ67 24点游戏算法        

```python
import itertools
a = input().split(' ')
b = []
for i in range(len(a)):
    b.append(int(a[i]))
c = list(itertools.permutations(b,4))
ending = False
chrs = []
for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(a)):
            temp = []
            if i == 0:
                temp.append('+')
            if i == 1:
                temp.append('-')
            if i == 2:
                temp.append('*')
            if i == 3:
                temp.append('/')
            if j == 0:
                temp.append('+')
            if j == 1:
                temp.append('-')
            if j == 2:
                temp.append('*')
            if j == 3:
                temp.append('/')
            if k == 0:
                temp.append('+')
            if k == 1:
                temp.append('-')
            if k == 2:
                temp.append('*')
            if k == 3:
                temp.append('/')
            chrs.append(list(temp))
for i in range(len(c)):
    for j in range(len(chrs)):
        temp = str(eval(str(c[i][0]) + chrs[j][0] + str(c[i][1])))
        temp = str(eval(temp + chrs[j][1] + str(c[i][2])))
        temp = eval(temp + chrs[j][2] + str(c[i][3]))
        if temp == 24:
            ending = True
if ending == True:
    print('true')
else:
    print('false')
```

HJ68 成绩排序          

```python
a = int(input())
b = int(input())
c = []
for i in range(a):
    c.append(input())
ending = []
temp = list(c)
if b == 0:
    for i in range(len(c)):
        max_position = -1
        max_value = -1
        for j in range(len(temp)):
            if int(temp[j].split(' ')[1]) > max_value:
                max_position = j
                max_value = int(temp[j].split(' ')[1])
        ending.append(temp[max_position])
        temp.remove(temp[max_position])
else:
    for i in range(len(c)):
        min_position = -1
        min_value = 200
        for j in range(len(temp)):
            if int(temp[j].split(' ')[1]) < min_value:
                min_position = j
                min_value = int(temp[j].split(' ')[1])
        ending.append(temp[min_position])
        temp.remove(temp[min_position])
for i in range(len(ending)):
    print(ending[i])
```

HJ69 矩阵乘法         

```python
a = int(input())
b = int(input())
c = int(input())
A = []
B = []
C = []
for i in range(a):
    temp = input().split(' ')
    A.append([])
    for j in range(len(temp)):
        A[i].append(int(temp[j]))
for i in range(b):
    temp = input().split(' ')
    B.append([])
    for j in range(len(temp)):
        B[i].append(int(temp[j]))
for i in range(a):
    C.append([])
    for k in range(c):
        temp_value = 0
        for j in range(b):
            temp_value = temp_value + A[i][j] * B[j][k]
        C[i].append(temp_value)
for i in range(len(C)):
    ending = ''
    for j in range(len(C[i])):
        if j == 0:
            ending = ending + str(C[i][j])
        else:
            ending = ending + ' ' + str(C[i][j])
    print(ending)
```

HJ70  矩阵乘法计算量估算              

```python
ending = 0
a = int(input())
b = []
for i in range(a):
    b.append(input())
c = input()
stack = []
calculate = []
alpha_number_1 = 0
for i in range(len(c)):
        if c[i].isalpha():
            stack.append(c[i])
            calculate.append(b[alpha_number_1].split(' '))
            alpha_number_1 += 1
        if c[i] == '(':
            stack.append(c[i])
        if c[i] == ')':
            alpha_number = 0
            while True:
                if len(stack) == 0:
                    break
                if stack[len(stack) - 1] == '(':
                    stack.pop()
                    break
                alpha_number += 1
                if alpha_number >= 2:
                    ending = ending + int(calculate[len(calculate) - 2][0]) * int(calculate[len(calculate) - 2][1]) * int(calculate[len(calculate) - 1][1])
                    temp_1 = int(calculate[len(calculate) - 2][0])
                    temp_2 = int(calculate[len(calculate) - 1][1])
                    #print(stack)
                    #print(calculate)
                    calculate.pop()
                    calculate.pop()
                    stack.pop()
                    stack.pop()
                    calculate.append([temp_1,temp_2])
print(ending)
```

HJ72 百钱买百鸡问题              

```python
a = input()
l = []
ending = []
for i in range(100):
    for j in range(100 - i):
        l.append([i,j,100-i-j])
for i in range(len(l)):
    if l[i][0] * 5 + l[i][1] * 3 + l[i][2] * (1 / 3) == 100:
        ending.append(l[i])
for i in range(len(ending)):
    temp = ''
    for j in range(len(ending[i])):
        if j == 0:
            temp = temp + str(ending[i][j])
        else:
            temp = temp + ' ' + str(ending[i][j])
    print(temp)
```

HJ73 计算日期到天数转换            

```python
#润年：4的倍数且不是100的倍数，或400的倍数
ending = 0
a = input().split(' ')
months = [31,28,31,30,31,30,31,31,30,31,30]
runnian = 0
if int(a[0]) % 400 == 0:
    runnian = 1
if int(a[0]) % 4 == 0 and int(a[0]) % 100 != 0:
    runnian = 1
if runnian == 1:
    months[1] = 29
if int(a[1]) == 1:
    ending = int(a[2])
else:
    for i in range(int(a[1]) - 1):
        ending = ending + months[i]
    ending = ending + int(a[2])
print(ending)
```

HJ74 参数解析           

```python
ending = []
a = input().split(' ')
flag = 0
temp = ''
for i in range(len(a)):
    time = 0
    for j in range(len(a[i])):
        if a[i][j] == '"':
            time += 1
    if time == 2:
        ending.append(a[i])
        continue
    if flag == 0:
        if not '"' in a[i]:
            ending.append(a[i])
        else:
            flag = 1
            temp = temp + a[i]
    else:
        temp = temp + ' ' + a[i]
        if '"' in a[i]:
            flag = 0
            ending.append(temp)
            temp = ''
print(len(ending))
for i in range(len(ending)):
    print(ending[i].replace('"', ''))
```

HJ75 公共子串计算            

```python
while True:
    try:
        a = input()
        b = input()
        n = 0
        for i in range(len(a)):
            if a[i-n:i+1] in b:
                n += 1
        print(n)
    except:
        break
```

HJ76 尼科彻斯定理            

```python
ending = 0
a = int(input())
b = a ** 3
c = a ** 2
if a % 2 == 0:
    ending = str(int(a ** 2 - 1)) + '+' + str(int(a ** 2 + 1))
    for i in range(int(a / 2 - 1)):
        ending = str(int(a ** 2 - 3 - 2 * i)) + '+' + ending + '+' + str(int(a ** 2 + 3 + 2 * i))
else:
    ending = str(int(a ** 2))
    for i in range(int(a / 2)):
        ending = str(int(a ** 2 - 2 - 2 * i)) + '+' + ending + '+' + str(int(a ** 2 + 2 + 2 * i))
print(ending)
```

HJ77 火车进站            

```python
#即按顺序入栈然后出栈
a = int(input())
b = input().replace(' ','')
ending = []
def function(stack, sequence, left_string):
    if len(left_string) == 0 and len(stack) == 0:
        if not sequence in ending:
            ending.append(sequence)
    else:
        if len(stack) == 0:
            stack.append(left_string[0])
            function(list(stack), sequence, left_string[1:len(left_string)])
        else:
            temp = stack[len(stack) - 1]
            if len(left_string) == 0:
                stack.pop()
                function(stack, sequence + temp,'')
            else:
                stack.append(left_string[0])
                function(list(stack), sequence, left_string[1:len(left_string)])
                stack.pop()
                stack.pop()
                function(list(stack), sequence + temp, left_string[0:len(left_string)])
function([],'',b)
ending.sort()
for i in range(len(ending)):
    temp = ending[i][0]
    for j in range(len(ending[i]) - 1):
        temp = temp + ' ' + ending[i][j + 1]
    print(temp)


```

HJ80 整型数组合并         

```python
a = int(input())
b = input().split(' ')
c = int(input())
d = input().split(' ')
f = []
for i in range(len(b)):
    f.append(int(b[i]))
g = []    
for i in range(len(d)):
    g.append(int(d[i]))
e = list(set(f + g))
e.sort()
ending = ''
for i in range(len(e)):
    ending = ending + str(e[i])
print(ending)
```

HJ81 字符串字符匹配          

```python
ending = 'true'
a = input()
b = input()
for i in range(len(a)):
    if not a[i] in b :
        ending = 'false'
print(ending)
```

HJ84 统计大写字母个数         

```python
ending = 0
a = input()
for i in range(len(a)):
    if a[i].isupper():
        ending += 1
print(ending)
```

HJ85 最长回文子串                 

```python
a = input()
n = 0
for i in range(len(a) - 1):
        temp = 0
        for j in range(i + 1):
            if i + 1 + j >= len(a):
                break
            if not a[i - j] == a[i + 1 + j]:
                break
            else:
                temp += 1
        if temp * 2 > n:
            n = temp * 2

        temp = 1
        for j in range(i):
            if i + 1 + j >= len(a) or i - j - 1 < 0:
                break
            if not a[i - j - 1] == a[i + 1 + j]:
                break
            else:
                temp += 2
        if temp  > n:
            n = temp
print(n)
```

HJ86 求最大连续bit数         

```python
ending = 0
a = bin(int(input())).replace('0b','')
temp = 0
for i in range(len(a)):
    if a[i]== '1':
        temp += 1
        if temp > ending:
            ending = temp
    else:
        temp = 0
print(ending)
```

HJ87 密码强度等级          

```python
ending = 0
a = input()
if len(a) <= 4:
    ending += 5
else:
    if len(a) <= 7:
        ending += 10
    else:
        ending += 25
#print(ending)
flag_1 = 0
for i in range(len(a)):
    if a[i].isupper():
        if flag_1 == 2:
            flag_1 = 3
        if flag_1 == 0:
            flag_1 = 1
    if a[i].islower():
        if flag_1 == 1:
            flag_1 = 3
        if flag_1 == 0:
            flag_1 = 2
if flag_1 == 1 or flag_1 == 2:
    ending += 10
if flag_1 == 3:
    ending += 20
#print(ending)
flag_2 = 0
for i in range(len(a)):
    if a[i].isdigit():
        flag_2 += 1
if flag_2 == 1:
    ending += 10
if flag_2 > 1:
    ending += 20
#print(ending)
flag_3 = 0
for i in range(len(a)):
    if (not a[i].isdigit()) and (not a[i].isalpha()):
        flag_3 += 1
if flag_3 == 1:
    ending += 10
if flag_3 > 1:
    ending += 25
#print(ending)
if flag_1 != 0 and flag_2 != 0 and flag_3 == 0:
    ending += 2
if (flag_1 == 1 or flag_1 == 2) and flag_2 != 0 and flag_3 != 0:
    ending += 3
if flag_1 == 3 and flag_2 != 0 and flag_3 != 0:
    ending += 5
if ending >= 90:
    print('VERY_SECURE')
else:
    if ending >= 80:
        print('SECURE')
    else:
        if ending >= 70:
            print('VERY_STRONG')
        else:
            if ending >= 60:
                print('STRONG')
            else:
                if ending >= 50:
                    print('AVERAGE')
                else:
                    if ending >= 25:
                        print('WEAK')
                    else:
                        print('VERY_WEAK')
```

HJ90 合法IP           

```python
ending = True
a = input().split('.')
for i in range(len(a)):
    if not a[i].isdigit():
        ending = False
        break
    if len(a[i]) > 1:
        if a[i][0] == '0':
            ending = False
    if not (int(a[i]) >= 0 and int(a[i]) <=255):
        ending = False
if len(a) != 4:
    ending = False
if ending:
    print('YES')
else:
    print('NO')
```

HJ91 走方格的方案数           

```python
a = input()
a = str(int(a.split(' ')[0]) + 1) + ' ' + str(int(a.split(' ')[1]) + 1)
ending = []
def function(position,way):
    if position == a:
        if not way in ending:
            ending.append(way)
    else:
        if position.split(' ')[0] != a.split(' ')[0]:
            function(str(int(position.split(' ')[0]) + 1) + ' ' + position.split(' ')[1],way + position)
        if position.split(' ')[1] != a.split(' ')[1]:
            function(position.split(' ')[0] + ' ' + str(int(position.split(' ')[1]) + 1), way + position)

function('1 1','')
print(len(ending))
```

HJ92 在字符串中找出连续最长的数字串            

```python
ending_string = ''
ending = 0
a = input()
temp = 0
position = 0
for i in range(len(a)):
    if not a[i].isdigit():
        temp = 0
    else:
        temp += 1
        if temp > ending:
            ending = temp
            position = i
temp = 0
for i in range(len(a)):
    if not a[i].isdigit():
        temp = 0
    else:
        temp += 1
        if temp == ending:
            position = i
            ending_string = ending_string + a[position - ending + 1:position + 1]
print(ending_string + ',' + str(ending))
```

HJ93 数组分组           

```python
def function(list_1, list_2, list_left):
    global ending
    if len(list_left) == 0:
        temp_1 = 0
        temp_2 = 0
        for i in range(len(list_1)):
            temp_1 += list_1[i]
        for i in range(len(list_2)):
            temp_2 += list_2[i]
        if temp_1 == temp_2:
             ending = True
    else:
        temp = list_left[len(list_left) - 1]
        temp_list = list(list_left)
        temp_list.pop()
        list_1.append(temp)
        function(list(list_1), list(list_2), temp_list)
        list_1.pop()
        list_2.append(temp)
        function(list(list_1), list(list_2), temp_list)

ending = False
a = int(input())
b = input().split(' ')
c = []
for i in range(len(b)):
    if b[i] != '':
        c.append(int(b[i]))
l_1 = []
l_2 = []
left = []
for i in range(len(c)):
    if c[i] % 5 == 0:
        l_1.append(c[i])
    else:
        if c[i] % 3 == 0:
            l_2.append(c[i])
        else:
            left.append(c[i])
function(l_1,l_2,left)
if ending:
    print('true')
else:
    print('false')
```

HJ94 记票统计             

```python
a = int(input())
b = input().split(' ')
c = int(input())
d = input().split(' ')
ending = []
ending .append(0)
for i in range(len(b)):
    ending.append(0)
sum_votes = 0
for i in range(len(b)):
    for j in range(len(d)):
        if b[i] == d[j]:
            ending[i] += 1
            sum_votes += 1
ending[a] = c - sum_votes
for i in range(len(b)):
    print(b[i] + " : " + str(ending[i]))
print('Invalid : ' + str(ending[a]))
```

HJ96 表示数字         

```python
a = input()
ending = ''
for i in range(len(a)):
    if not a[i].isdigit():
        ending = ending + a[i]
    else:
        if i == 0:
            if len(a) == 1:
                ending = '*' + str(a[i]) + '*'
            else:
                ending = '*' + str(a[i])
                if not a[i + 1].isdigit():
                    ending = ending + '*'
        else:
            if i == len(a) - 1:
                if a[i - 1].isdigit():
                    ending = ending + str(a[i]) + '*'
                else:
                    ending = ending + '*' + str(a[i]) + '*'
            else:
                if a[i - 1].isdigit():
                    if not a[i + 1].isdigit():
                        ending = ending + str(a[i]) + '*'
                    else:
                        ending = ending + str(a[i])
                else:
                    ending = ending + '*' + str(a[i])
                    if not a[i + 1].isdigit():
                        ending = ending + '*'
print(ending)
```

HJ97 记负均正         

```python
a = int(input())
b = input().split(' ')
c = []
ending_1 = 0
ending_2 = 0
ending_3 = ''
temp = 0
for i in range(len(b)):
    c.append(int(b[i]))
for i in range(len(c)):
    if c[i] < 0:
        ending_1 += 1
    else:
        if c[i] != 0:
            #print(c[i])
            ending_2 += c[i]
        else:
            temp += 1
if a - ending_1 - temp != 0:
    ending_2 = ending_2 / (a - ending_1 - temp)
if '.' in str(ending_2):
    if (ending_2 - int(ending_2)) % 0.1 >=0.05:
        ending_2 += 0.1
        print(str(ending_1) + ' ' + str(ending_2).split('.')[0] + '.' + str(ending_2).split('.')[1][0])
    else:
        print(str(ending_1) + ' ' + str(ending_2).split('.')[0] + '.' + str(ending_2).split('.')[1][0])
else:
    print(str(ending_1) + ' ' + str(ending_2) + '.0')
```

HJ99 自守数        

```python
ending = 0
a = int(input())
for i in range(a + 1):
    temp = str(int(i ** 2))
    if temp[len(temp) - len(str(i)):len(temp)] == str(i):
        ending += 1
print(ending)
```

HJ100 等差数列

```python
a = int(input())
ending = 0
temp = []
for i in range(a):
    temp.append(3 * i + 2)
for i in range(len(temp)):
    ending += temp[i]
print(ending)
```

HJ101 输入整型数组和排序标识，对其元素按照升序或降序进行排序

```python
a = int(input())
b = input().split(' ')
c = input()
d = []
ending = ''
for i in range(len(b)):
    d.append(int(b[i]))
d.sort()
for i in range(len(d)):
    if c == '0':
        if i == 0:
            ending = ending + str(d[i])
        else:
            ending = ending + ' ' + str(d[i])
    else:
        if i == 0:
            ending = ending + str(d[len(d) - i - 1])
        else:
            ending = ending + ' ' + str(d[len(d) - i - 1])
print(ending)
```

HJ102 字符统计          

```python
#两种判断用两种循环分别判断，满足第一个条件的选出来，再遍历满足第二个条件的
a = input()
b = list(set(list(a)))
ending = []
show = ''
for i in range(len(b)):
    temp = 0
    for j in range(len(a)):
        if b[i] == a[j]:
            temp += 1
    ending.append(str(temp) + b[i])
ending.sort()
show = ''
temp_l_1 = []
for i in range(len(ending)):
    max_value = -1
    min_char = 100000
    position = -1
    if i == 0:
        temp_l_1 = list(ending)
    for j in range(len(temp_l_1)):
        if int(temp_l_1[j][0:len(temp_l_1[j]) - 1]) >= max_value:
            max_value = int(temp_l_1[j][0:len(temp_l_1[j]) - 1])
    for j in range(len(temp_l_1)):
        if int(temp_l_1[j][0:len(temp_l_1[j]) - 1]) == max_value:
            if ord(temp_l_1[j][len(temp_l_1[j]) - 1]) < min_char:
                min_char = ord(temp_l_1[j][len(temp_l_1[j]) - 1])
                position = j
    show = show + temp_l_1[position][len(temp_l_1[position]) - 1]
    temp_l_1.remove(temp_l_1[position])
print(show)
```

HJ103 Redraiment的走法               

```python
#最长递增子序列
ending = 0

def function(step, height, l_left):
    global ending
    if len(l_left) == 0:
        if step > ending:
            ending = step
    else:
        temp_l = list(l_left)
        temp_l.pop()
        if height < l_left[len(l_left) - 1]:
            function(step + 1, l_left[len(l_left) - 1], list(temp_l))
            function(step, height, list(temp_l))
        else:
            function(step, height, list(temp_l))


a = int(input())
b = input().split(' ')
c = []
# 倒着添加的
for i in range(len(b)):
    c.append(int(b[len(b) - i - 1]))
temp = []
temp = list(c)
for i in range(len(c)):
    if i == len(c) - 1:
        if ending <= 0:
            ending = 1
        break
    aa = temp[len(temp) - 1]
    temp.pop()
    function(1, aa, list(temp))
print(ending)
```

HJ106 字符逆序         

```python
a = input()
print(a[::-1])
```

HJ107 求解立方根           

```python
ending = 0
a = float(input())
flag = 0
if a < 0:
    flag = 1
    a = -a
flag_1 = 0
if a < 1:
    a = a * 1000
    flag_1 = 1
def function(range_left, range_right):
    global a, ending
    value = (range_left + range_right) / 2
    if abs(value ** 3 - a) <= 0.08:
        ending = value
    else:
        if value ** 3 > a:
            function(range_left, value)
        else:
            function(value, range_right)
function(0, a)
if flag == 1:
    ending = -ending
if flag_1 == 1:
    ending = ending / 10
print("%.1f" %ending)
```

HJ108 求最小公倍数             

```python
#先算质数
def get_max_zhishu(value):
    ending = 1
    i = 1
    while True:
        i += 1
        if value % i == 0:
            value = int(value / i)
            ending = i
        if value <= i:
            break
    return ending
ending = 0
temp = input().split(' ')
a = int(temp[0])
b = int(temp[1])
c = get_max_zhishu(a)
d = get_max_zhishu(b)
i = 0
while True:
    i += 1
    if c == d:
        if (c * i) % a== 0 and (c * i) % b== 0:
            print(c * i)
            break
    else:
        if (d * c * i) % a == 0 and (d * c * i) % b == 0:
            print(d * c * i)
            break
```

```
给定一个整数num和一个数字k，求解一个连续递增数列，使得长度为k的数列之和为num，存在该数列时输出数列，不存在时输出-1

例如：

输入 525 6

输出 85 86 87 88 89 90


输入 1 3

输出 -1
```

```python
a = input()
b = int(a.split(' ')[0])
c = int(a.split(' ')[1])
base = 0
ending = -1
ending_1 = []
for i in range(c):
    base = base + i + 1
for i in range(b):
    if c * i + base == b:
        break
temp = i
if temp != b - 1:
    for i in range(c):
        ending_1.append(temp + i + 1)
    print(' '.join(str(i) for i in ending_1))
else:
    print(ending)

```

```
给一个只包含大写字母的字符串，（字符串长度大于0），和一个数字k，

记录连续的相同字符的出现次数，并按出现次数排序，输出排第k位的字母的出现次数，不存在时输出-1（如果一个字母出现多次则只保留最高次数的记录，如果几个字母出现次数相同则按原字符串的出现顺序排序）

输入 AAAHHHHBHHHDDCCC

        3

输出 3

分析：最终记录结果应为 { H：4次，A：3次，H：3次（忽略），C：3次，D：2次，B：1次}，排第三位的应该是C：3次，因此输出3
```

```python
a = input()
number = int(input())
b = []
start = 0
for i in range(len(a) - 1):
    if a[i] != a[i + 1]:
        b.append(a[start:i + 1])
        start = i + 1
        if i == len(a) - 2:
            b.append(a[i - 1])
    else:
        if i == len(a) - 2:
            b.append(a[start:i + 2])
ending = []
temp = list(b)
temp_1 = list(b)
for i in range(len(b)):
    max_length = -1
    position = -1
    for j in range(len(temp_1)):
        if len(temp_1[j]) > max_length:
            max_length = len(temp_1[j])
            position = j
    temp_2 = list(temp_1)
    for j in range(len(temp_1)):
        if temp_1[position][0] in temp_1[j]:
            temp_2.remove(temp_1[j])
    if max_length > 0:
        ending.append(max_length)
    temp_1 = list(temp_2)
print(ending[number - 1])
```

```
给一个纯数字字符串，和一个数字k，求该字符串删掉k个数字后组成数字的最小值

  输入：2615371

             4

  输出：131

  分析：令‘2635131’整个字符串中删掉四个数，保留的结果最小，即删掉2，6，5，7后剩余131是最小的
```

```python
a = input()
b = int(input())
c = list(a)
for i in range(b):
    temp = list(c)
    for j in range(len(c) - 1):
        if int(c[j]) > int(c[j + 1]):
            del temp[j]
            break
    c = temp
ending = ''
for i in range(len(c)):
    ending += c[i]
print(ending)
```

```
用数组代表每个人的权重，现在要进行组队权重大于等于 N，每个队可以由 1人或 2人组队，且 1个人只能参加 1个队，
计算可以派出最多的符合要求的团队

输入三行

第一行：代表数组长度

第二行：数组的元素

第三行：最小权重

示例：

5

3 1 5 7 9

8

输出： 3 解释： [ 3 5 ] [ 1 7 ] [ 9 ]
```

```python
a = input()
b = sorted(input().split(' '))
c = int(input())
ending = 0
d = []
for i in range(len(b)):
    if int(b[i]) < c:
        d.append(int(b[i]))
ending = ending + len(b) - len(d)
start_point = 0
end_point = len(d) - 1
for i in range(len(d)):
    if start_point >= end_point:
        break
    for j in range(end_point - start_point):
        if int(d[end_point]) + int(d[start_point + j]) >= c:
            start_point += j
            end_point += -1
            ending += 1
            break
print(ending)
```

```
最大嵌套括号深度
题目描述：
现有一字符串仅由 ‘(’， ‘)’， ‘{’， ‘}’， ‘[’， ']'六种括号组成。 若字符串满足以下条件之一，则为无效字符串：

①任一类型的左右括号数量不相等；
②存在未按正确顺序（先左后右）闭合的括号。
输出括号的最大嵌套深度，若字符串无效则输出 0。 0≤字符串长度≤100000

输入描述:
一个只包括 ‘(’， ‘)’， ‘{’， ‘}’， ‘[’， ']'的字符串

输出描述：
一个整数，最大的括号深度

示例 1：

输入
[]
输出
1
说明
有效字符串，最大嵌套深度为1

示例 2：

输入
([]{()})
输出
3
说明
有效字符串，最大嵌套深度为3

示例 3：

输入
(]
输出
0
说明
无效字符串，有两种类型的左右括号数量不相等

示例 4：

输入
([)]
输出
0
说明
无效字符串，存在未按正确顺序闭合的括号
```

```python
a = input()
stack = []
max_depth = 0
temp_1 = 0
for i in range(len(a)):
    if a[i] in '({[':
        stack.append(a[i])
        if temp_1 > max_depth:
            max_depth = temp_1
            temp_1 = 0
    else:
        temp = len(stack) - 1
        if (stack[temp] == '(' and a[i] == ')') or \
                (stack[temp] == '[' and a[i] == ']') or \
                (stack[temp] == '{' and a[i] == '}'):
            stack.pop()
            temp_1 += 1
    if temp_1 > max_depth and i == len(a) - 1:
        max_depth = temp_1
        temp_1 = 0
if len(stack) == 0:
    print(max_depth)
else:
    print(0)
```

```
请实现一个简易内存池,根据请求命令完成内存分配和释放。
内存池支持两种操作命令，REQUEST和RELEASE，其格式为：
REQUEST=请求的内存大小 表示请求分配指定大小内存，如果分配成功，返回分配到的内存首地址；如果内存不足，或指定的大小为0，则输出error。
RELEASE=释放的内存首地址 表示释放掉之前分配的内存，释放成功无需输出，如果释放不存在的首地址则输出error。
注意：
1.内存池总大小为100字节。
2.内存池地址分配必须是连续内存，并优先从低地址分配。
3.内存释放后可被再次分配，已释放的内存在空闲时不能被二次释放。
4.不会释放已申请的内存块的中间地址。
5.释放操作只是针对首地址所对应的单个内存块进行操作，不会影响其它内存块。
解答要求
时间限制: 1000ms, 内存限制: 256MB
首行为整数 N , 表示操作命令的个数，取值范围：0 < N <= 100。
接下来的N行, 每行将给出一个操作命令，操作命令和参数之间用 “=”分割。

输入输出
样例1：
2
REQUEST=10
REQUEST=20
输出样例1：
0
10

样例2：
5
REQUEST=10
REQUEST=20
RELEASE=0
REQUEST=20
REQUEST=10
输出样例2：
0
10
30
0

提示说明：
第一条指令，申请地址0~9的10个字节内存，返回首地址0
第二条指令，申请地址10~29的20字节内存，返回首地址10
第三条指令，释放首地址为0的内存申请，0~9地址内存被释放，变为空闲，释放成功，无需输出
第四条指令，申请20字节内存，09地址内存连续空间不足20字节，往后查找到3049地址，返回首地址30
第五条指令，申请10字节，0~9地址内存空间足够，返回首地址0
```

```python
def function(l, command, number):
    if command[2] == 'Q':
        postion = -1
        space = 0
        for i in range(100):
            if postion == -1 and l[i] == 0:
                postion = i
                space += 1
            if space == number:
                break
            if l[i] != 0:
                postion = -1
                space = 0
            if postion != -1 and l[i] == 0:
                space += 1
        if space == number:
            l[100] += 1
            print(postion)
            for i in range(number):
                l[postion + i] = l[100]
    else:
        if number == 0 and l[0] != 0:
            for i in range(100):
                if l[i] == l[i + 1]:
                    l[i] = 0
                else:
                    l[i] = 0
                    break
        if number != 0 and l[number] != 0 and l[number -1] != l[number]:
            for i in range(100- number):
                if l[number + i] == l[number + i + 1]:
                    l[number + i] = 0
                else:
                    l[number + i] = 0
                    break

a = int(input())
b = []
memory = []
for i in range(a):
    b.append(input())
for i in range(101):
    if i == 100:
        memory.append(100)
        break
    memory.append(0)
for i in  range(a):
    function(memory, b[i].split('=')[0], int(b[i].split('=')[1]))
```

```
给定一个正整数数组
检查数组中是否存在满足规则的数组组合
规则：
 A=B+2C
输入描述
 第一行输出数组的元素个数
 接下来一行输出所有数组元素  用空格隔开
输出描述
 如果存在满足要求的数
 在同一行里依次输出 规则里 A/B/C的取值 用空格隔开
 如果不存在输出0

 示例1：
   输入
   4
   2 7 3 0
   输出
   7 3 2
   说明：
    7=3+2*2
   示例2：
   输入
    3
    1 1 1
   输出
    0
    说明找不到满足条件的组合

    备注：
    数组长度在3~100之间
    数组成员为0~65535
    数组成员可以重复
    但每个成员只能在结果算式中使用一次
    如 数组成员为 [0,0,1,5]
    0出现两次允许，但结果0=0+2*0不允许  因为算式中使用了3个0
```

```python
import itertools
a = int(input())
b = input().split( )
c = []
d = []
flag = 0
for i in range(len(b)):
    c.append(int(b[i]))
for e in itertools.permutations(c,3):
    d.append(e)
for i in range(len(d)):
    if d[i][0] == d[i][1] * 2 + d[i][2]:
        print(str(d[i][0]) + ' ' + str(d[i][1]) + ' ' + str(d[i][2]))
        flag = 1
if flag == 0:
    print(0)
```

```
347. 前 K 个高频元素
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]

提示：

1 <= nums.length <= 105
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的
```

```python
class Solution:
    ending = ''
    def function(self,s):
        l_1 = list(s)
        start_position = -1
        end_position = -1
        used_positions = 0
        for i in range(len(s)):
            temp = used_positions
            if s[i] == '(':
                start_position = i
                used_positions = 0
            if s[i] == ')' and start_position != -1:
                end_position = i
                used_positions = 0
            if not s[i] in '()':
                used_positions += 1
            if end_position - start_position == 1:
                l_1[start_position] = '0'
                l_1[end_position] = '0'
                break
            if end_position - start_position == temp + 1:
                l_1[start_position] = '0'
                l_1[end_position] = '0'
                break

        if ''.join(l_1) == s:
            self.ending = s
        else:
            self.function(''.join(l_1))
    def longestValidParentheses(self, s):
        max_value = 0
        l = []
        self.function(s)
        temp = 0
        for i in range(len(self.ending)):
            if self.ending[i].isdigit():
                temp += 1
                max_value = max(max_value,temp)
            else:
                temp = 0
        return max_value
```

```
79. 单词搜索

给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。


示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

示例 2：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true

示例 3：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false
```

```python
#浅拷贝列表中含有列表的列表时需要自己写个函数实现
class Solution(object):
    ending = False
    example = []
    #浅拷贝列表中含有列表的列表时需要自己写个函数实现
    def new_board(self, source):
        l_1 = []
        for i in range(len(source)):
            l_1.append([])
            for j in range(len(source[0])):
                l_1[i].append(source[i][j])
        return l_1
    def function(self, board, position, word):
        self.example.append(word)
        if len(word) == 0:
            self.ending = True
        else:
            if position[0] < len(board) - 1 and \
                    board[position[0] + 1][position[1]] != '-1' and\
                    board[position[0] + 1][position[1]] == word[0]:
                temp = self.new_board(board)
                temp[position[0] + 1][position[1]] = '-1'
                self.function(temp, [position[0] + 1,position[1]], word[1:len(word)])
            if position[0] > 0 and \
                    board[position[0] - 1][position[1]] != '-1' and\
                    board[position[0] - 1][position[1]] == word[0]:
                temp = self.new_board(board)
                temp[position[0] - 1][position[1]] = '-1'
                self.function(temp, [position[0] - 1,position[1]], word[1:len(word)])
            if position[1] < len(board[0]) - 1 and \
                    board[position[0]][position[1] + 1] != '-1' and\
                    board[position[0]][position[1] + 1] == word[0]:
                temp = self.new_board(board)
                temp[position[0]][position[1] + 1] = '-1'
                self.function(temp, [position[0],position[1] + 1], word[1:len(word)])
            if position[1] > 0 and \
                    board[position[0]][position[1] - 1] != '-1' and\
                    board[position[0]][position[1] - 1] == word[0]:
                temp = self.new_board(board)
                temp[position[0]][position[1] - 1] = '-1'
                self.function(temp, [position[0],position[1] - 1], word[1:len(word)])

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        #先判断从前面和后面怎么搜更快
        forward = 0
        backward = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    forward += 1
                if board[i][j] == word[len(word) - 1]:
                    backward += 1
        if backward < forward:
            useless = word[::-1]
            word = useless

        self.ending = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    temp = self.new_board(board)
                    print(board)
                    print(temp)
                    temp[i][j] = '-1'
                    self.function(list(temp),[i,j],word[1:len(word)])
        return self.ending
```

```
32. 最长有效括号

给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

 

示例 1：

输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"
示例 2：

输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"
示例 3：

输入：s = ""
输出：0
```

```python
#一次处理一个的递归
class Solution:
    ending = ''
    def function(self,s):
        l_1 = list(s)
        start_position = -1
        end_position = -1
        used_positions = 0
        for i in range(len(s)):
            temp = used_positions
            if s[i] == '(':
                start_position = i
                used_positions = 0
            if s[i] == ')' and start_position != -1:
                end_position = i
                used_positions = 0
            if not s[i] in '()':
                used_positions += 1
            if end_position - start_position == 1:
                l_1[start_position] = '0'
                l_1[end_position] = '0'
                break
            if end_position - start_position == temp + 1:
                l_1[start_position] = '0'
                l_1[end_position] = '0'
                break

        if ''.join(l_1) == s:
            self.ending = s
        else:
            self.function(''.join(l_1))
    def longestValidParentheses(self, s):
        max_value = 0
        l = []
        self.function(s)
        temp = 0
        for i in range(len(self.ending)):
            if self.ending[i].isdigit():
                temp += 1
                max_value = max(max_value,temp)
            else:
                temp = 0
        return max_value
```


```python
#递归用全局变量表示结果
class Solution(object):
    function_ending = ''
    def function(self,function_string):
        temp_l = list(function_string)
        for i in range(len(function_string) - 1):
            if i != 0:
                if function_string[i - 1] == '(' and function_string[i + 1] == ')':
                    temp_l[i - 1] = '0'
                    temp_l[i + 1] = '0'
                    temp_l[i] = chr(ord(temp_l[i]) + 1)
        temp_s = ''.join(temp_l).replace('0','')
        temp_l = list(temp_s)
        for i in range(len(temp_s) - 1):
            if (not temp_s[i] in '()0' )and (not temp_s[i + 1] in '()0' ):
                if i > 0 and (temp_s[i - 1] in '()0' ):
                    temp_l[i] = chr(ord(temp_s[i]) + ord(temp_s[i + 1]) - ord('A') + 1)
                    temp_l[i + 1] = '0'
                if i == 0:
                    temp_l[i] = chr(ord(temp_s[i]) + ord(temp_s[i + 1]) - ord('A') + 1)
                    temp_l[i + 1] = '0'
        temp_s = ''.join(temp_l).replace('0', '')
        if temp_s != function_string:
            self.function(temp_s)
        else:
            self.function_ending = function_string

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = list(s)
        temp_string = ''
        for i in range(len(s) - 1):
            if s[i] == '(' and s[i + 1] == ')':
                temp[i] = '0'
                temp[i + 1] = '0'
                temp_string = ''.join(temp).replace('00','A')
        if 'A' in temp_string:
            self.function(temp_string)
            self.function_ending = self.function_ending.replace('(', '')
            self.function_ending = self.function_ending.replace(')', '')
            ending_1 = list(self.function_ending)
            ending_1.sort()
            print(ending_1)
            return 2 * (ord(ending_1[len(ending_1) - 1]) - ord('A') + 1)
        else:
            return 0
```

```
分糖果

现有几袋糖果，老师要将糖果分给小张和小王两个同学，每一袋都有一定数量的糖果，每袋糖果只能全部分给他们其中一人，要求最终两人分得糖果的数量相同。
         
             输入：糖果的袋数和各袋中糖果的数量；
             输出：平分下来的糖果数量，以及两个人分别分到的各袋中糖果的数量，如果无法平分，则直接输出-1
    
    -示例1：
              输入：
                    5
                    2 6 5 4 7
              输出：
                    12
                    2 4 6
                    5 7
    
    -示例2：
              输入：
                    4
                    1 2 3 5
              输出：
                    -1
```
```python
#深搜实现
#写递归时把退出条件写在最上面
ending = []
def dfs(l,weight):
    global a, target, ending
    if weight == target:
        ending = list(l)
    else:
        if weight < target:
            for i in range(len(l)):
                temp_l = []
                for j in range(len(l)):
                    if i != j:
                        temp_l.append(l[j])
                dfs(list(temp_l), weight + l[i])

a = int(input())
b = input().split()
c = []
target = 0
for i in range(len(b)):
    c.append(int(b[i]))
    target += int(b[i])
target = target / 2
c.sort()
maxmun = c[len(c) - 1]
c.pop()
dfs(list(c),maxmun)
print(ending)
```

```
硬件资源的最佳分配

有M台服务器，每台服务器包含属性：

编号(整数)，CPU核数(1-100)，内存(10-1000)，CPU架构(0-8)，是否支持NP加速卡标识(0,1)。

请根据资源分配要求分配N台满足要求的服务器。资源分配要求：

CPU核数>=cpuCount，内存>=memSize，CPU架构=cpuArch，是否支持NP卡=supportNP。其中，cpuCount、memSize、cpuArch、supportNP为输入的分配参数。

分配时同时会指定优选级策略strategy，策略如下：

策略1：CPU优先，表示优选CPU核数满足分配要求并最接近分配要求的cpuCount。当CPU核数相同时，再按内存满足要求并最接近memSize的服务器分配。

策略2：内存优先，表示优选内存满足分配要求并最接近分配要求的memSize。当内存相同时，再按CPU核数满足要求并最接近cpuCount的服务器分配。

如果两台服务器属性相同，则按服务器编号从小到大选择（编号不会重复）。

输入

第一行服务器数量M台

接下来M行为M台服务器属性的数组

紧接着下一行为分配要求：最大分配数量N，分配策略strategy，cpuCount，memSize，cpuArch，supportNP

其中：

1<=M<=1000

1<=N<=1000

strategy：1表示策略1，2表示策略2

1<=cpuCount<=100

10<=memSize<=1000

0<=cpuArch<=8，另外，cpuArch使用9表示所有CPU架构都满足分配要求

0<=supportNP<=1，另外，supportNP为2时表示不论是否支持NP卡都满足要求

输出

先输出实际分配数量，后续分配的服务器编号从小到大依次输出，以空格间隔

样例1

输入：4
     0,2,200,0,1
     1,3,400,0,1
     2,3,400,1,0
     3,3,300,0,1
     3 1 3 200 0 1
输出：2 1 3
解释：只有编号1和3满足要求，要求分配2台服务器，所以结果为2 1 3

样例2

输入：6
     0,2,200,0,1
     1,4,330,2,1
     2,3,400,3,1
     3,3,310,1,1
     4,3,320,8,1
     5,3,330,0,1
     3 2 3 300 9 2
输出：3 3 4 5
解释：编号为1 2 3 4 5都满足分配要求。要求按分配策略2分配，即内存优先策略，内存大于等于300并接近300依次是3 4 1 5 2.其中1和5内存相同，按分配策略2要求当内存相同时再比较CPU，即CPU大于等于3的并接近3的，所有5优先于1.因此最后分配3台服务器是3 4 5.先输出数量3，再按编号排序后输出3 4 5

样例3

输入：2
     0,2,200,1,0
     1,3,400,2,1
     2 2 3 300 3 2
输出：0
解释：都不满足cpuArch为3的要求
```

```python
a = int(input())
b = []
ending = []
for i in range(a):
    #编号（整数），CPU核数（1-100）、内存（10-1000）、CPU架构（0-8）、是否支持NP加速卡标识（0，1)
    b.append(input().split(','))
#策略1：CPU优先，表示优选CPU核数满足分配要求并最接分配要求的cpuCount.当CPU核数相同时，再按内存满足要求并最接近memSize的服务器分配。
#策略2：内存优先，表示优选内存满足分配要求并最接近分配要求的memsize.当内存相同时，再按CPU核数满足要求并最接i近cpuCount的服务器分配。
#最大分配数量N，分配策略srategy，cpuCount，memsize，cpuArch，supportNP
c = input().split(' ')
for i in range(len(b)):
    if (not int(b[i][1]) >= int(c[2])) or (not int(b[i][2]) >= int(c[3])):
        continue
    if (c[4] != '9') and c[4] != b[i][3]:
        continue
    if (c[5] != '2') and c[5] != b[i][4]:
        continue
    ending.append(b[i])
if int(c[0]) > len(ending):
    if len(ending) == 0:
        print(0)
    else:
        temp = str(len(ending))
        for i in range(len(ending)):
            temp = temp + ' ' + str(ending[i][0])
        print(temp)
else:
    temp_l = list(ending)
    ending = []
    if c[1] == '1':
        for j in range(int(c[0])):
            best_position = -1
            max_cpu = -1
            max_memory = -1
            for i in range(len(temp_l)):
                if int(temp_l[i][1]) > max_cpu:
                    best_position = i
            for i in range(len(temp_l)):
                if int(temp_l[i][2]) == max_memory and int(temp_l[i][1]) > max_cpu:
                    max_cpu = int(temp_l[i][1])
                    best_position = i
            ending.append(temp_l[best_position])
            temp_l.remove(temp_l[best_position])
    else:
        for j in range(int(c[0])):
            best_position = -1
            max_cpu = -1
            max_memory = -1
            for i in range(len(temp_l)):
                if int(temp_l[i][2]) > max_memory:
                    best_position = i
            for i in range(len(temp_l)):
                if int(temp_l[i][1]) == max_cpu and int(temp_l[i][2]) > max_memory:
                    max_memory = int(temp_l[i][2])
                    best_position = i
            ending.append(temp_l[best_position])
            temp_l.remove(temp_l[best_position])
    temp = str(len(ending))
    s = []
    for i in range(len(ending)):
        s.append(int(ending[i][0]))
    s.sort()
    for i in range(len(s)):
        temp = temp + ' ' + str(s[i])
    print(temp)
```

```
题目描述：

给定一个射击比赛成绩单，包含多个选手若干次射击的成绩分数，请对每个选手按其最高三个分数之和进行降序排名，输出降序排名后的选手id序列。
题目解析：

给一个数字表示射击的次数，然后给几个选手进行（乱序）射击，生成对应的成绩！
条件如下：

一个选手可以有多个射击成绩的分数，且次序不固定
如果一个选手成绩少于3个，则认为选手的所有成绩无效，排名忽略该选手
如果选手的成绩之和相等，则相等的选手按照其id降序排列
输入描述：

输入第一行，一个整数N，表示该场比赛总共进行了N次射击，产生N个成绩分数（2<=N<=100）
输入第二行，一个长度为N整数序列，表示参与每次射击的选手id（0<=id<=99）
输入第三行，一个长度为N整数序列，表示参与每次射击选手对应的成绩（0<=成绩<=100）
输出描述：

符合题设条件的降序排名后的选手ID序列

示例

输入：

31
3,3,7,4,4,4,4,7,7,3,5,5,5
53,80,68,24,39,76,66,16,100,55,53,80,55
输出：

5,3,7,4
说明:

该场射击比赛进行了13次，参赛的选手为{3,4,5,7}
3号选手成绩53,80,55 最高三个成绩的和为188
4号选手成绩24,39,76,66 最高三个成绩的和为205
5号选手成绩53,80,55 最高三个成绩的和为188
7号选手成绩68,16,100 最高三个成绩的和为184
比较各个选手最高3个成绩的和，有4号>3号=5号>7号，由于3号和5号成绩相等，且id 5>3，所以输出 7,5,3,4
```

```python
#一对多时用字典
a = int(input())
b = input().split(',')
c = input().split(',')
dic = {}
ending = ''
for i in range(len(b)):
    if b[i] in dic.keys():
        dic[b[i]] = dic[b[i]] + ' ' + c[i]
    else:
        dic[b[i]] = c[i]
temp = []
for i in dic.keys():
    if len(dic[i].split(' '))  < 3:
        temp.append(i)
for i in range(len(temp)):
    dic.pop(temp[i])
for i in dic.keys():
    temp = dic[i].split(' ')
    for j in range(len(temp)):
        temp[j] = int(temp[j])
    temp.sort()
    temp_1 = 0
    for j in range(3):
        temp_1 += temp[len(temp) - 1 - j]
    dic[i] = temp_1
for i in sorted(dic, key=dic.__getitem__):
    ending = ending + ',' + i
print(ending[1:len(ending)][::-1])
```

```
任务调度器

给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。

然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的 最短时间 。

 

示例 1：

输入：tasks = ["A","A","A","B","B","B"], n = 2
输出：8
解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B
     在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。 
示例 2：

输入：tasks = ["A","A","A","B","B","B"], n = 0
输出：6
解释：在这种情况下，任何大小为 6 的排列都可以满足要求，因为 n = 0
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
诸如此类
示例 3：

输入：tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
输出：16
解释：一种可能的解决方案是：
     A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> (待命) -> (待命) -> A -> (待命) -> (待命) -> A

```

```python
'''
构建一个 最多的任务数 * (n + 1)的二维数组
假设把最多的任务放到列表的第一列，其余元素增添在列表里都符合条件
统计最后一行元素书 + 最多的任务数 - 1行的位置个数即可
最后是在总任务数和结果中取最大值
A B C
A B D
A B
'''
from collections import Counter
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        dic = Counter(tasks)
        a = max(dic.values())
        last_row = sum([1 for i in dic.values() if i == a])
        return max(len(tasks),  last_row + (a - 1) * (n + 1))
```

```
字符串分割

将字符串分割成一些子串，使每个子串的ASClI码值的和均为水仙花数（水仙花数就是各位的立方之和等于本身的数）。
1、若分割不成功，则返回0

2、若分割成功且分割结果不唯一，则返回-1

3、若分割成功且分割结果唯一，则返回分割后子串的数目

 

输入：abc

输出：0（说明：分割不成功）

 

输入：f3@d5a8

输出：-1（说明：分割成功且结果不唯一。结果1：f3和@d5a8，结果2：f3@d5和a8）

 

输入：AXdddF

输出：2（说明：分割成功且结果唯一：AX和dddF）


字符串最大长度为200
```

```python
#一个子串开头应该是水仙花数，或本身就是水仙花数
shuixianshu = []
ending = []
def is_shuixianshu(s_list):
    global shuixianshu
    if s_list in shuixianshu:
        return True
    temp_ending = sum(s_list)
    if len(str(temp_ending)) == 3:
        if int(str(temp_ending)[0]) ** 3 + int(str(temp_ending)[1]) ** 3 + int(str(temp_ending)[2]) ** 3 == temp_ending:
            shuixianshu.append(s_list)
            return True
        else:
            return False

def function(s_list,temp_ending):
    function_ending = list(temp_ending)
    if len(s_list) == 0:
        ending.append(temp_ending)
    else:
        for i in range(len(s_list)):
            if is_shuixianshu(s_list[0:i + 1]):
                function_ending.append(s_list[0:i + 1])
                function(s_list[i + 1:],function_ending)

a = list(input())
a = [ord(i) for i in a]
temp_ending = []
function(a,temp_ending)
if len(ending) == 0:
    print(0)
if len(ending) == 1:
    print(len(ending[0]))
if len(ending) > 1:
    print(-1)
```

leetcode 394. 字符串解码          

```python
class Solution(object):
    def decodeString(self, s):
        stack, ending, base = [], '', 0
        for i in range(len(s)):
            if s[i].isdigit():
                base = base * 10 + int(s[i])
            if s[i].isalpha():
                ending = ending + s[i]
            if s[i] == '[':
                stack.append((ending,base))
                ending, base = '', 0
            if s[i] == ']':
                (temp_1, temp_2) = stack.pop()
                ending = temp_1 + temp_2 * ending
        return ending
```

```
题目描述：

某通信网络中有N个网络结点，用1到N进行标识。
网络中的结点互联互通，且结点之间的消息传递有时延，相连结点的时延均为一个时间单位。
现给定网络结点的连接关系link[i]={u，v}，其中u和v表示网络结点。
当指定一个结点向其他结点进行广播，所有被广播结点收到消息后都会在原路径上回复一条响应消息，请计算发送结点至少需要等待几个时间单位才能收到所有被广播结点的响应消息。
注：

N的取值范围为[1，100];
连接关系link的长度不超过3000，且1 <= u,v <= N;
网络中任意结点间均是可达的;
输入描述：

输入的第一行为两个正整数，分别表示网络结点的个数N，以及时延列表的长度T；
接下来的T行输入，表示结点间的连接关系列表；
最后一行的输入为一个正整数，表示指定的广播结点序号；
输出描述：

输出一个整数，表示发送结点接收到所有响应消息至少需要等待的时长。
示例：

　　输入：

　　5 7
　　1 4
　　2 1
　　2 3
　　2 4
　　3 4
　　3 5
　　4 5
　　2

　　输出：

　　4
```

```python
#无需递归的广搜
def bfs(table):
    global a,b
    touched_nodes = []
    depth = 0
    my_queue = [b]
    touched_nodes.append(b)
    while True:
        if len(touched_nodes) == int(a[0]):
            break
        depth += 1
        temp_list = []
        for i in my_queue:
            for j in table[i - 1]:
                if not j in touched_nodes:
                    temp_list.append(j)
                    touched_nodes.append(j)
        my_queue = list(temp_list)
    return depth
a = input().split()
nodes = []
b = 0
while True:
    get_temp = input()
    if ' ' in get_temp:
        nodes.append(get_temp.split(' '))
    else:
        b = int(get_temp)
        break
nodes_list = []
for i in range(int(a[0])):
    nodes_list.append([])
    for j in nodes:
        if j[0] ==str(i + 1):
            nodes_list[i].append(int(j[1]))
        if j[1] ==str(i + 1):
            nodes_list[i].append(int(j[0]))
print(bfs(nodes_list) * 2)
```

```
    // 在一条笔直的公路上安装了N个路灯，从位置0开始安装，路灯之间间距固定为100m。每个路灯都有⾃⼰的照明半径，请计算第一个路灯和最后
    // 一个路灯之间，无法照明的区间的长度和。
    // 输入描述：
    // 第一行为一个数N，表示路灯个数，1<=N<=100000
    // 第二行为N个空格分隔的数，表示路径的照明半径，1<=照明半径<=100000*100
    // 输出描述：
    // 第一个路灯和最后一个路灯之间，无法照明的区间的长度和
    // 例1：
    // 输入
    // 2
    // 50 50
    // 输出
    // 0
```