---
layout: post
title: 3种join算法的实现
categories: [CS, PYTHON]
tags: [python]
---
<!-- more --> 
```mysql
关系R具有两个属性A和B，其中A和B的属性值均为int型（4个字节），A的值域为[1, 40]，B的值域为[1, 1000]。              
关系S具有两个属性C和D，其中C和D的属性值均为int型（4个字节）。C的值域为[20, 60]，D的值域为[1, 1000]。               
1）实现关系选择算法：实现关系选择算法，选出R.A=40或S.C=60的元组，并将结果存放在磁盘上。                
2）实现关系投影算法：实现关系投影算法，对关系R上的A属性进行投影，并将结果存放在磁盘上。                
3）实现Nested-Loop Join (NLJ)算法：基于ExtMem程序库，使用C语言实现NLJ算法，对关系R和S计算R.A连接S.C，并将结果存放在磁盘上。               
```

```python
import os
import random
import math
class relationship():
    def __init__(self,name,properties=["DEFALT_0","DEFALT_1"],minimums=[0,0],maximums=[1,1]):
        '''
        初始化关系对象
        :param name: 关系名
        :param properties:属性名的list
        :param minimums:属性值域最小值的list
        :param maximums:属性值域最大值的list
        '''
        self.name = name
        self.properties = properties
        self.minimums = minimums
        self.maximums = maximums
        #tuples 中存储了属性个list，属性的角标和属性对应list 在tuples中角标相同
        self.tuples =[]
        self.properties_amount = len(self.properties)
        for i in range(len(self.properties)):
            self.tuples.append([])
        print("关系 " + self.name + " 已成功创建")

    def add_tuple(self,property,tuple_value):
        '''
        向关系中根据属性添加元素
        :param property: 属性
        :param tuple_value: 元素的值
        '''
        for i in range(len(self.properties)):
            if self.properties[i] == property:
                if tuple_value <= self.maximums[i] and tuple_value >= self.minimums[i]:
                    self.tuples[i].append(tuple_value)
                    print("%d 已经成功添加到关系 %s 的属性 %s 中"%(tuple_value,self.name,property))
                    break
                else:
                    print("%d 不在 %d 和 %d 之间"%(tuple_value,self.minimums[i],self.maximums[i]))
                    break
            else:
                if i == len(self.properties) - 1:
                    print("关系 " + self.name + " 中不存在属性 " + property)

    def Write_Text(self,file_name, contant):
        '''
        将string写入指定的文件中
        :param file_name: 文件名
        :param contant: 待写入的string
        :return:
        '''
        with open(file_name, "w") as f:
            f.writelines(contant)
            f.writelines("\n")

    def write_to_disk(self):
        '''
        将对象中的信息写入到磁盘中
        '''
        path = os.path.abspath('.')
        disk_path = path + "\disk"
        relationship_path = disk_path + "\\" + self.name
        if not os.path.exists(disk_path):
            os.mkdir(disk_path)
            print("创建文件夹 %s"%(disk_path))
        if not os.path.exists(relationship_path):
            os.mkdir(relationship_path)
            print("创建文件夹 %s"%(relationship_path))
        relationship.Write_Text(self, relationship_path + "\\" + "properties.txt",str(self.properties))
        relationship.Write_Text(self, relationship_path + "\\" + "minimums.txt", str(self.minimums))
        relationship.Write_Text(self, relationship_path + "\\" + "maximums.txt", str(self.maximums))
        relationship.Write_Text(self, relationship_path + "\\" + "tuples.txt", str(self.tuples))

    def Read_Text(self,file_name):
        '''
        读文件的第一行
        :param file_name:待读文件路径
        :return: 待读文件内容的第一行
        '''
        f = open(file_name, "r")
        return f.readline()

    def read_from_disk(self):
        '''
        从磁盘中读入该对象名对应的信息并复制给该对象中的字段
        '''
        path = os.path.abspath('.')
        disk_path = path + "\disk"
        relationship_path = disk_path + "\\" + self.name
        if not os.path.exists(relationship_path):
            print("数据库中不存在关系 %s" % (self.name))
        else:
            self.properties = (relationship.Read_Text(
                self,relationship_path + "\\" + "properties.txt").replace("[","").replace("]","")).replace("'","").replace("\n","").split(",")
            temp = (relationship.Read_Text(
                self,relationship_path + "\\" + "minimums.txt").replace("[","").replace("]","")).replace("'","").replace("\n","").split(",")
            self.minimums = [int(i) for i in temp]
            temp = (relationship.Read_Text(
                self, relationship_path + "\\" + "maximums.txt").replace("[", "").replace("]", "")).replace("'",
                                                                                                            "").replace(
                "\n", "").split(",")
            self.maximums = [int(i) for i in temp]
            temp = relationship.Read_Text(self, relationship_path + "\\" + "tuples.txt").split(", [")
            temp_0 = []
            for i in range(len(temp)):
                if i == 0:
                    temp_0.append(
                        [int(j) for j in temp[i].replace("[[","").replace("]","").replace("'","").split(",")])
                if i == len(temp) - 1:
                    temp_0.append(
                        [int(j) for j in temp[i].replace("]]", "").replace("[", "").replace("'", "").split(",")])
            self.tuples = temp_0

    def select(self,property,value):
        '''
        根据属性和值选择内容
        :param property: 属性
        :param value: 值
        :return: 结果的list
        '''
        ending = []
        ending.append(self.properties)
        for i in range(len(self.properties)):
            if self.properties[i] == property:
                for j in range(len(self.tuples[i])):
                    if (self.tuples[i])[j] == value:
                        temp = []
                        for k in range(len(self.tuples)):
                            temp.append((self.tuples[k][j]))
                        ending.append(temp)
        path = os.path.abspath('.')
        disk_path = path + "\disk"
        select_path = disk_path + "\select_" + property+ "=" + str(value) + "_from_" + self.name + ".txt"
        relationship.Write_Text(self,select_path,str(ending))
        print("选择%s.%s = %s :"%(self.name,property,str(value)))
        print(ending)
        print("")
        return ending

    def project(self,properties):
        '''
        投影且去重
        :param properties:想要投影的属性
        :return:投影且去重的结果的list,list中第一个元素为属性名
        return example:
        [['A'], [24], [31], [26], [28], [40]]
        '''
        ending = []
        temp = []
        amount = len(properties)
        for i in range(len(properties)):
            for j in range(len(self.properties)):
                if self.properties[j] == properties[i]:
                    temp.append(self.tuples[j])
        for i in range(len(self.tuples[0])):
            temp_in =[]
            for j in range(amount):
                temp_in.append((temp[j])[i])
            ending.append(temp_in)
        new_ending = []
        new_ending.append(properties)
        for id in ending:
            if id not in new_ending:
                new_ending.append(id)
        path = os.path.abspath('.')
        disk_path = path + "\disk"
        project_path = disk_path + "\project_" + str(properties) + "_from_" + self.name + ".txt"
        relationship.Write_Text(self, project_path, str(new_ending))
        print_ending = str(self.name) + "."
        for i in range(len(properties)):
            print_ending = print_ending + properties[i]
        print("投影 %s : "%(print_ending))
        print(new_ending)
        print("")
        return new_ending

    def get_single_list(self,property):
        '''
        由属性获得对应的list
        :param property: 属性名
        :return: 属性名对应的list
        '''
        for i in range(len(self.properties)):
            if property == self.properties[i]:
                return self.tuples[i].copy()

    def insert_sort(self,property):
        '''
        升序的插入排序
        :param property:排序的依据属性
        '''
        for i in range(len(self.properties)):
            if property == self.properties[i]:
                for j in range(len(self.tuples[i])):
                    for k in range(j):
                        if self.tuples[i][j] < self.tuples[i][k]:
                            for l in range(len(self.tuples)):
                                self.tuples[l].insert(k,self.tuples[l].pop(j))
                break

    def get_same_position(self,property):
        '''
        对于已经排序过的list而言，获取同值/单个元素的首个元素位置
        :param property: 元素对应的属性
        :return: 同值/单个元素的首个元素位置对应的list
        '''
        ending = []
        for i in range(len(self.properties)):
            if property == self.properties[i]:
                now_value = self.tuples[i][0]
                ending.append(0)
                for j in range(len(self.tuples[i])):
                    if now_value != self.tuples[i][j]:
                        now_value = self.tuples[i][j]
                        ending.append(j)
        return ending

def nest_loop_join(relationships,buffer_sizes,properties):
    '''
    通过nest loop join算法进行关系的连接
    :param relationships: 两个relationship对象构成的list
    :param buffer_sizes: 两个relationship各自对应的缓冲区大小构成的list
    :param properties: 两个relationship各自对应的连接的属性的list
    :return:连接结果的list，list中第一个元素为属性名
    return example:
    [['A', 'B', 'C', 'D'], [20, 654, 20, 792], [33, 972, 33, 160], [33, 467, 33, 160]]
    '''
    ending = []
    #用copy方法，否则temp和右侧的指向同一地址!!!
    temp = relationships[0].properties.copy()
    temp_1 = relationships[1].properties
    for i in range(len(temp_1)):
        temp.append(temp_1[i])
    ending.append(temp)
    for i in range(len(relationships[0].properties)):
        if properties[0] == relationships[0].properties[i]:
            list_0 = relationships[0].tuples[i]
    for i in range(len(relationships[1].properties)):
        if properties[1] == relationships[1].properties[i]:
            list_1 = relationships[1].tuples[i]
    for i in range(math.ceil((len(list_0)) / buffer_sizes[0])):
        for j in range(math.ceil((len(list_1)) / buffer_sizes[1])):
            for k in range(buffer_sizes[0]):
                for l in range(buffer_sizes[1]):
                    position_0 = (i * buffer_sizes[0] + k)
                    position_1 = (j * buffer_sizes[1] + l)
                    if position_0 < len(list_0) and position_1 < len(list_1):
                        if list_0[position_0] == list_1[position_1]:
                            temp_in = []
                            for i_in in range(len(relationships[0].tuples)):
                                temp_in.append(((relationships[0].tuples)[i_in])[position_0])
                            for i_in in range(len(relationships[1].tuples)):
                                temp_in.append(((relationships[1].tuples)[i_in])[position_1])
                            ending.append(temp_in)
    print("nest loop join 计算 %s.%s 与 %s.%s 连接的结果如下 :"%(
        relationships[0].name,properties[0],relationships[1].name,properties[1]))
    print(ending)
    print("")
    return ending

def hash(single_relationship,property,partitions_number=8):
    '''
    计算指定关系中的属性的每个元组中值的取余hash值，并返回hash值对应的元素在原关系中的角标的list的list
    :param single_relationship: 想要计算hash的关系
    :param property: 想要计算hash的属性
    :param partitions_number: hash时分成的桶数（组数）
    :return: hash值对应的元素在原关系中的角标的list的list
    return example:
    当关系中有20个元组，分成8组时
    [[0, 14], [10], [4], [2, 3, 5, 11], [9, 16], [6, 7, 15], [1, 12, 17, 19], [8, 13, 18]]
    '''
    ending = []
    for i in range(partitions_number):
        ending.append([])
    temp = []
    for i in range(len(single_relationship.properties)):
        if property == single_relationship.properties[i]:
            temp = single_relationship.tuples[i]
            break
    for i in range(len(temp)):
        ending[temp[i] % partitions_number].append(i)
    return ending


def hash_join(relationships,properties,partitions_number=8):
    '''
    通过hash join算法进行关系的连接
    :param relationships: 两个relationship对象构成的list
    :param properties: 两个relationship各自对应的连接的属性的list
    :param partitions_number: hash时分成的桶数（组数）
    :return: 连接结果的list，list中第一个元素为属性名
    return example:
    [['A', 'B', 'C', 'D'], [25, 353, 25, 986], [34, 309, 34, 597]]
    '''
    ending = []
    temp = relationships[0].properties.copy()
    temp_1 = relationships[1].properties
    for i in range(len(temp_1)):
        temp.append(temp_1[i])
    ending.append(temp)
    list_0 = relationships[0].get_single_list(properties[0])
    list_1 = relationships[1].get_single_list(properties[1])
    hash_list_0 = hash(relationships[0],properties[0],partitions_number)
    hash_list_1 = hash(relationships[1], properties[1], partitions_number)
    for i in range(partitions_number):
        for j in range(len(hash_list_0[i])):
            for k in range(len(hash_list_1[i])):
                position_0 = (hash_list_0[i])[j]
                position_1 = (hash_list_1[i])[k]
                if list_0[position_0] == list_1[position_1]:
                    temp_in = []
                    for i_in in range(len(relationships[0].tuples)):
                        temp_in.append(((relationships[0].tuples)[i_in])[position_0])
                    for i_in in range(len(relationships[1].tuples)):
                        temp_in.append(((relationships[1].tuples)[i_in])[position_1])
                    ending.append(temp_in)
    print("hash join 计算 %s.%s 与 %s.%s 连接的结果如下 :" % (
    relationships[0].name, properties[0], relationships[1].name, properties[1]))
    print(ending)
    print("")
    return ending

def sorted_join(lists):
    '''
    计算两个lists中的已经升序排序了的lists[0]和lists[1]值相同的元素在各自的list中的位置
    :param lists:两个待连接的list的list
    :return:一个list的而原数组，lists[0]的ending[i][0] 位置和lists[1]的ending[i][j] j!=0位置的元素值相同
    return example:
    [[12, 0, 1], [13, 0, 1], [14, 0, 1], [15, 0, 1], [16, 2], [17, 2], [18, 3, 4, 5, 6, 7], [19, 3, 4, 5, 6, 7]]
    '''

    ending = []
    if lists[0][len(lists[0]) - 1] < lists[1][0]:
        ending = None
    else:
        start = 0
        for i in range(len(lists[0])):
            start_change_flag = 0
            temp = []
            for j in range(start,len(lists[1])):
                if lists[1][j] == lists[0][i]:
                    if start_change_flag == 0:
                        start_change_flag = 1
                        start = j
                        temp.append(i)
                        temp.append(j)
                    else:
                        temp.append(j)
                if lists[1][j] > lists[0][i]:
                    break
            if not len(temp) == 0:
                ending.append(temp)
    return ending


def sort_merge_join(relationships,buffer_sizes,properties):
    '''
    通过sort merge join算法进行关系的连接
    :param relationships:两个relationship对象构成的list
    :param properties: 两个relationship各自对应的连接的属性的list
    :param buffer_sizes:两个relationship各自对应的缓冲区大小构成的list
    :return:连接结果的list，list中第一个元素为属性名
    return example:
    [['A', 'B', 'C', 'D'], [20, 429, 20, 482], [20, 429, 20, 326], [20, 665, 20, 482]]
    '''
    ending = []
    temp = relationships[0].properties.copy()
    temp_1 = relationships[1].properties
    for i in range(len(temp_1)):
        temp.append(temp_1[i])
    ending.append(temp)
    relationships[0].insert_sort(properties[0])
    relationships[1].insert_sort(properties[1])
    for i in range(len(relationships[0].properties)):
        if properties[0] == relationships[0].properties[i]:
            list_0 = relationships[0].tuples[i]
    for i in range(len(relationships[1].properties)):
        if properties[1] == relationships[1].properties[i]:
            list_1 = relationships[1].tuples[i]
    lists_0 = []
    block_number_0 = math.ceil((len(list_0)) / buffer_sizes[0])
    for i in range(block_number_0):
        if i == block_number_0 - 1:
            lists_0.append(list_0[i * buffer_sizes[0]:len(list_0)])
        else:
            lists_0.append(list_0[i * buffer_sizes[0]:(i + 1) * buffer_sizes[0]])
    lists_1 = []
    block_number_1 = math.ceil((len(list_1)) / buffer_sizes[1])
    for i in range(block_number_1):
        if i == block_number_1 - 1:
            lists_1.append(list_1[i * buffer_sizes[1]:len(list_1)])
        else:
            lists_1.append(list_1[i * buffer_sizes[1]:(i + 1) * buffer_sizes[1]])
    list_ending = []
    for i in range(block_number_0):
        start = 0
        start_changed_flag = 0

        for j in range(start,block_number_1):
            temp_2 = sorted_join([lists_0[i],lists_1[j]])
            if temp_2 == None:
                break
            for k in range(len(temp_2)):
                temp_2[k][0] = temp_2[k][0] + i * buffer_sizes[0]
                for l in range(len(temp_2[k]) - 1):
                    temp_2[k][l + 1] = temp_2[k][l + 1] + j * buffer_sizes[1]
            if start_changed_flag == 0:
                start = j
                start_changed_flag = 1
            list_ending.append(temp_2)
    for i in range(len(list_ending)):
        for j in range(len(list_ending[i])):
            for k in range(len(list_ending[i][j]) - 1):
                temp_in = []
                for i_in in range(len(relationships[0].tuples)):
                    temp_in.append(((relationships[0].tuples)[i_in])[list_ending[i][j][0]])
                for i_in in range(len(relationships[1].tuples)):
                    temp_in.append(((relationships[1].tuples)[i_in])[list_ending[i][j][k + 1]])
                ending.append(temp_in)
    print("sort merge join 计算 %s.%s 与 %s.%s 连接的结果如下 :" % (
        relationships[0].name, properties[0], relationships[1].name, properties[1]))
    print(ending)
    return ending

if __name__ == '__main__':
    R = relationship("R", ["A", "B"], [1, 1], [40, 1000])
    S = relationship("S", ["C", "D"], [20, 1], [60, 1000])
    for i in range(100):
        R.add_tuple("A", random.randint(1, 40))
        R.add_tuple("B", random.randint(1, 1000))
        S.add_tuple("C", random.randint(20, 60))
        S.add_tuple("D", random.randint(1, 1000))
    R.select("A", 40)
    R.project(["A"])
    R.project(["A","B"])
    nest_loop_join([R,S],[20,20],["A","C"])
    hash_join([R,S],["A","C"],8)
    sort_merge_join([R,S],[20,20],["A","C"])

    '''
    R = relationship("R",["A","B"],[1,1],[40,1000])
    S = relationship("S", ["C", "D"], [20, 1], [60, 1000])
    R.read_from_disk()
    S.read_from_disk()
    '''

    '''
        for i in range(30):
        R.add_tuple("A", random.randint(1, 40))
        R.add_tuple("B", random.randint(1, 1000))
        S.add_tuple("C", random.randint(20, 60))
        S.add_tuple("D", random.randint(1, 1000))
    R.write_to_disk()
    S.write_to_disk()
    R.select("A",40)
    S.select("C",60)
    R.project(["A"])
    R.project(["A","B"])
    R.properties
    '''
    '''
    extmen = em.ExtMem()
    extmen.getNewBlockInBuffer()
    extmen.write_to_buffer(nima)
    extmen = em.ExtMem()
    extmen.getNewBlockInBuffer()
    extmen.write_to_buffer(nima)
    '''
```
