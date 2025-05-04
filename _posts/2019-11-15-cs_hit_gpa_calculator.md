---
layout: post
title: hit gpa calculator 
---
<!-- more -->
score_calculator.py
```python
from matplotlib import pyplot as plt

def function(file_path):
    '''
    可以根据实际课程类型增添contains - replace
    :param file_path:成绩路径
    :return: 各阶段成绩
    '''
    score_list = []
    X = []
    X_0 = []
    ending = 0
    total_weight = 0
    i = 0
    for line in open(file_path, "r", encoding='utf-8', errors='ignore'):
        if line.__contains__("取消资格"):
            continue
        if line.__contains__("旷考"):
            continue
        if line.__contains__("是"):
            line = line.replace("是", "")
        if line.__contains__("其他"):
            line = line.replace("其他", "")
        if line.__contains__("创新MOOC"):
            line = line.replace("创新MOOC", "")
        if line.__contains__("MOOC"):
            line = line.replace("MOOC", "")
        if line.__contains__("任选"):
            line = line.replace("任选", "")
        if line.__contains__("必修"):
            line = line.replace("必修", "")
        if line.__contains__("素质核心"):
            line = line.replace("素质核心", "")
        if line.__contains__("素质选修"):
            line = line.replace("素质选修", "")
        if line.__contains__("选修"):
            line = line.replace("选修", "")
        if line.__contains__("限选"):
            line = line.replace("限选", "")
        lines = line.split(".", 1)  # 最多只根据"."分成两份

        integer = int(lines[0][-1])
        decimal = int(lines[1][0])
        weight = integer + 0.1 * decimal  # 学分

        if lines[1].__contains__("补"):
            one_score = 60
        else:
            temp = float(lines[1].replace("				", "")[1:5])
            if temp < 60:
                continue
            else:
                one_score = float(lines[1].replace("				", "")[1:5])
        ending = ending + one_score * weight
        total_weight = total_weight + weight
        print(ending / total_weight)
        score_list.append(ending / total_weight)
        i = i + 1
        X.append(total_weight)
        X_0.append(one_score)
    print("现成绩 : " + str(ending / total_weight))
    print("科目数 : " + str(i))
    print("总学分 : " + str(total_weight))
    score = score_list
    Y = score
    plt.plot(X, Y, "m:")
    plt.plot(X, Y, "c.")
    #plt.plot(X, X_0, "y.")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()



#从jwes复制成绩
function("score.txt")
```
score.txt is copy from jwes.hit.edu.cn      
example:     
```
2	2017秋季	学工处	AD12401	成功心理与人才发展	任选	素质核心	2.0				取消资格	取消资格	304
```
