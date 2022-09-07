touched_nodes = []
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
a = ['5','7']
b = 2

print(bfs([[4, 2], [1, 3, 4], [2, 4, 5], [1, 2, 3, 5], [3, 4]]))




