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
print(bfs(nodes_list))




