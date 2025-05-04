---
layout: post
title: 将mysql查询语句转化为查询树
---
<!-- more --> 
```mysql
任选下列查询语句中的三条，将其转化为对应的查询执行树，并且根据设计的查询优化算法，对生成的查询执行树进行优化。              
SELECT [ ENAME = ’Mary’ & DNAME = ’Research’ ] ( EMPLOYEE JOIN DEPARTMENT )                  
PROJECTION [ BDATE ] ( SELECT [ ENAME = ’John’ & DNAME = ’ Research’ ] ( EMPLOYEE JOIN DEPARTMENT) )                   
SELECT [ ESSN = ’01’ ] (  PROJECTION [ ESSN, PNAME ] ( WORKS_ON JOIN PROJECT ) )                  
PROJECTION [ ENAME ] ( SELECT [ SALARY < 3000 ] ( EMPLOYEE JOIN SELECT [ PNO = ’P1’ ] ( WORKS_ON JOIN PROJECT ) )                  
PROJECTION [ DNAME, SALARY ] ( AVG [ SALARY ] ( SELECT [ DNAME = ’ Research’ ] ( EMPLOYEE  JOIN  DEPART MENT) )                 
```

```python
from pptree import *


def parser(sentence):
    '''
    将输入的数据库查询序列解析成表tables的list，选择条件selects的list，投影projections的list
    假设以上三个list中的元素按list的角标对应
    以及绘制查询树并优化
    :param sentence:sql查询语句
    :return: tables,selects,projections 三个list组成的list
    return example：
    [['EMPLOYEE', 'DEPARTMENT'], [['ENAME', '=', 'Mary'], ['DNAME', '=', 'ENAME']], []]
    '''
    temp = sentence.replace("[", "").replace("]", "").replace("(", "").replace(")", "").replace("’", "").replace(",",
                                                                                                                 "").split(
        " ")
    temp_0 = []
    for i in range(len(temp)):
        if temp[i] != "":
            temp_0.append(temp[i])
    tables = []
    for i in range(len(temp_0)):
        if temp_0[i] == "JOIN":
            tables.append(temp_0[i - 1])
            tables.append(temp_0[i + 1])
    temp_1 = temp_0[0: i - 2]
    # sequence = 1 表示select在projection之前，为0则相反，为-1表示没有projection
    sequence = -2
    selects = []
    projections = []
    if not temp_1.__contains__("PROJECTION"):
        sequence = -1
    and_flag = 0
    for i in range(len(temp_1)):
        if (temp_1[i] == "&"):
            selects.append([temp_1[i - 3], temp_1[i - 2], temp_1[i - 1]])
            selects.append([temp_1[i + 1], temp_1[i + 2], temp_1[i - 3]])
            and_flag = 1
    if and_flag == 0:
        for i in range(len(temp_1)):
            if (temp_1[i] == "SELECT"):
                selects.append([temp_1[i + 1], temp_1[i + 2], temp_1[i + 3]])
    for i in range(len(temp_1)):
        if (temp_1[i] == "PROJECTION"):
            if i + 1 <= len(temp_1):
                if temp_1[i + 2] == "SELECT":
                    projections.append(temp_1[i + 1])
                    sequence = 0
                else:
                    projections.append(temp_1[i + 1])
                    projections.append(temp_1[i + 2])
                    sequence = 1
    print("lexer       : " + str(temp_0))
    print("tables      : " + str(tables))
    print("selects     : " + str(selects))
    print("projections : " + str(projections))
    # print(sequence)

    amend = 1
    if sequence == -1:
        root_1 = "SELECT " + "".join(selects[0])
        if len(selects) == 2:
            root_1 = root_1 + " " + "".join(selects[1])
        paint_root = Node(root_1)
        paint_join = Node("JOIN", paint_root)
        for i in range(len(tables)):
            Node(str(tables[i]), paint_join)
        print("原始查询树 :")
        print_tree(paint_root, horizontal=False)

        children = []
        paint_root = Node("JOIN")
        for i in range(len(selects)):
            children.append(Node("SELECT " + "".join(selects[i]), paint_root))
            Node(str(tables[i]), children[i])
        print("改进查询树(%d) :" % (amend))
        amend = amend + 1
        print_tree(paint_root, horizontal=False)

    if sequence == 0:
        root_1 = "PROJECTION " + "".join(projections[0])
        if len(projections) == 2:
            root_1 = root_1 + " " + "".join(selects[1])
        paint_root = Node(root_1)
        select_1 = "SELECT " + "".join(selects[0])
        if len(selects) == 2:
            select_1 = select_1 + " " + "".join(selects[1])
        paint_select = Node(select_1, paint_root)
        paint_join = Node("JOIN", paint_select)
        for i in range(len(tables)):
            Node(str(tables[i]), paint_join)
        print("原始查询树 :")
        print_tree(paint_root, horizontal=False)

        root_1 = "PROJECTION " + "".join(projections[0])
        if len(projections) == 2:
            root_1 = root_1 + " " + "".join(selects[1])
        paint_root = Node(root_1)
        select_1 = "SELECT " + "".join(selects[0])
        paint_select_1 = Node(select_1, paint_root)
        if len(selects) == 2:
            select_2 = "SELECT " + " " + "".join(selects[1])
            paint_select_2 = Node(select_2, paint_select_1)
            paint_join = Node("JOIN", paint_select_2)
            for i in range(len(tables)):
                Node(str(tables[i]), paint_join)
        else:
            paint_join = Node("JOIN", paint_select_1)
            for i in range(len(tables)):
                Node(str(tables[i]), paint_join)
        print("改进查询树(%d) :" % (amend))
        amend = amend + 1
        print_tree(paint_root, horizontal=False)

        root_1 = "PROJECTION " + "".join(projections[0])
        if len(projections) == 2:
            root_1 = root_1 + " " + "".join(selects[1])
        paint_root = Node(root_1)
        paint_join = Node("JOIN", paint_root)
        join_children = []
        for i in range(len(selects)):
            join_children.append(Node("SELECT " + "".join(selects[i]), paint_join))
            Node(str(tables[i]), join_children[i])
        print("改进查询树(%d) :" % (amend))
        amend = amend + 1
        print_tree(paint_root, horizontal=False)

        root_1 = "PROJECTION " + "".join(projections[0])
        if len(projections) == 2:
            root_1 = root_1 + " " + "".join(selects[1])
        paint_root = Node(root_1)
        paint_join = Node("JOIN", paint_root)
        join_children = []
        join_children.append(Node(root_1 + " DNO", paint_join))
        Node(str(tables[0]), Node("SELECT " + "".join(selects[0]), join_children[0]))
        join_children.append(Node("PROJECTION DNO", paint_join))
        Node(str(tables[1]), Node("SELECT " + "".join(selects[1]), join_children[1]))
        print("改进查询树(%d) :" % (amend))
        print("假设BDATE为EMPLOYEE的属性,假设DNO为EMPLOYEE和DEPARTMENT的共同属性,代表部门编号")
        amend = amend + 1
        print_tree(paint_root, horizontal=False)

    if sequence == 1:
        root_1 = "SELECT " + "".join(selects[0])
        if len(selects) == 2:
            root_1 = root_1 + " " + "".join(selects[1])
        paint_root = Node(root_1)
        str_projections = "PROJECTION " + "".join(projections[0])
        if len(projections) == 2:
            str_projections = str_projections + " " + "".join(projections[1])
        paint_projection = Node(str_projections, paint_root)
        paint_join = Node("JOIN", paint_projection)
        for i in range(len(tables)):
            Node(str(tables[i]), paint_join)
        print("原始查询树 :")
        print_tree(paint_root, horizontal=False)

        str_projections = "PROJECTION " + "".join(projections[0])
        if len(projections) == 2:
            str_projections = str_projections + " " + "".join(projections[1])
        paint_root = Node(str_projections)
        str_select = "SELECT " + "".join(selects[0])
        if len(selects) == 2:
            str_select = str_select + " " + "".join(selects[1])
        paint_select = Node(str_select, paint_root)
        paint_join = Node("JOIN", paint_select)
        for i in range(len(tables)):
            Node(str(tables[i]), paint_join)
        print("改进查询树(%d) :" % (amend))
        amend = amend + 1
        print_tree(paint_root, horizontal=False)

        str_projections = "PROJECTION " + "".join(projections[0])
        if len(projections) == 2:
            str_projections = str_projections + " " + "".join(projections[1])
        paint_root = Node(str_projections)
        paint_join = Node("JOIN", paint_root)
        str_select = "SELECT " + "".join(selects[0])
        if len(selects) == 2:
            str_select = str_select + " " + "".join(selects[1])
        Node(str(tables[0]), Node(str_select, paint_join))
        Node(str(tables[1]), paint_join)
        print("改进查询树(%d) :" % (amend))
        print("假设ESSN是WORKS_ON的属性")
        amend = amend + 1
        print_tree(paint_root, horizontal=False)

        str_projections = "PROJECTION " + "".join(projections[0])
        if len(projections) == 2:
            str_projections = str_projections + " " + "".join(projections[1])
        paint_root = Node(str_projections)
        paint_join = Node("JOIN", paint_root)
        str_select = "SELECT " + "".join(selects[0])
        paint_projection = []
        for i in range(len(projections)):
            paint_projection.append(Node("PROJECTION " + str(projections[i]) + " PNO ", paint_join))
        Node(str(tables[0]), Node(str_select, paint_projection[0]))
        Node(str(tables[1]), paint_projection[1])
        print("改进查询树(%d) :" % (amend))
        print("假设ESSN是WORKS_ON的属性，假设PNO为WORKS_ON和PROJECT的共同属性")
        amend = amend + 1
        print_tree(paint_root, horizontal=False)
    print("")
    return [tables, selects, projections]


if __name__ == '__main__':
    assignments = []
    assignments.append("SELECT [ ENAME = ’Mary’ & DNAME = ’Research’ ] ( EMPLOYEE JOIN DEPARTMENT )")
    # 假设BDATE为 EMPLOYEE的属性,假设DNO为EMPLOYEE和DEPARTMENT的共同属性,代表部门编号
    assignments.append(
        "PROJECTION [ BDATE ] ( SELECT [ ENAME = ’John’ & DNAME = ’ Research’ ] ( EMPLOYEE JOIN DEPARTMENT) )")
    # 假设ESSN是WORKS_ON的属性，假设PNO为WORKS_ON和PROJECT的共同属性
    assignments.append("SELECT [ ESSN = ’01’ ] (  PROJECTION [ ESSN, PNAME ] ( WORKS_ON JOIN PROJECT ) )")
    for i in range(3):
        parser(assignments[i])

```