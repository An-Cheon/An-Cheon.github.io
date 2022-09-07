---
layout: post
title: 数据结构
---
<!-- more -->
树
```python
class NodeTree:
    def __init__(self, root=None, lchild=None, rchild=None):
        """创建二叉树
        Argument:
            lchild: BinTree
                左子树
            rchild: BinTree
                右子树

        Return:
            Tree
        """
        self.root = root
        self.lchild = lchild
        self.rchild = rchild


class BinTree:

    # -----------前序遍历 ------------
    # 递归算法
    def pre_order_recursive(self, T):
        if T == None:
            return
        print(T.root, end=' ')
        self.pre_order_recursive(T.lchild)
        self.pre_order_recursive(T.rchild)

    # -----------中序遍历 ------------
    # 递归算法
    def mid_order_recursive(self, T):
        if T == None:
            return
        self.mid_order_recursive(T.lchild)
        print(T.root, end=' ')
        self.mid_order_recursive(T.rchild)

    # -----------后序遍历 ------------
    # 递归算法
    def post_order_recursive(self, T):
        if T == None:
            return
        self.post_order_recursive(T.lchild)
        self.post_order_recursive(T.rchild)
        print(T.root, end=' ')

    # ----------- 前序遍历序列、中序遍历序列 —> 重构二叉树 ------------
    def tree_by_pre_mid(self, pre, mid):
        if len(pre) != len(mid) or len(pre) == 0 or len(mid) == 0:
            return
        T = NodeTree(pre[0])
        index = mid.index(pre[0])
        T.lchild = self.tree_by_pre_mid(pre[1:index + 1], mid[:index])
        T.rchild = self.tree_by_pre_mid(pre[index + 1:], mid[index + 1:])
        return T

    # ----------- 后序遍历序列、中序遍历序列 —> 重构二叉树 ------------
    def tree_by_post_mid(self, post, mid):
        if len(post) != len(mid) or len(post) == 0 or len(mid) == 0:
            return
        T = NodeTree(post[-1])
        index = mid.index(post[-1])
        T.lchild = self.tree_by_post_mid(post[:index], mid[:index])
        T.rchild = self.tree_by_post_mid(post[index:-1], mid[index + 1:])
        return T


if __name__ == '__main__':
    # ----------- 测试：前序、中序、后序、层次遍历 -----------
    # 创建二叉树
    nodeTree = NodeTree(1,
                        lchild=NodeTree(2,
                                        lchild=NodeTree(4,
                                                        rchild=NodeTree(7))),
                        rchild=NodeTree(3,
                                        lchild=NodeTree(5),
                                        rchild=NodeTree(6)))
    T = BinTree()
    T.pre_order_recursive(nodeTree)  # 前序遍历-递归
    print('\n')
    T.mid_order_recursive(nodeTree)  # 中序遍历-递归
    print('\n')
    T.post_order_recursive(nodeTree)  # 后序遍历-递归
    print('\n')

    print('==========================================================================')

    # ----------- 测试：由遍历序列构造二叉树 -----------
    T = BinTree()
    pre = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    mid = ['B', 'C', 'A', 'E', 'D', 'G', 'H', 'F', 'I']
    post = ['C', 'B', 'E', 'H', 'G', 'I', 'F', 'D', 'A']

    newT_pre_mid = T.tree_by_pre_mid(pre, mid)  # 由前序序列、中序序列构造二叉树
    T.post_order_recursive(newT_pre_mid)  # 获取后序序列
    print('\n')

    newT_post_mid = T.tree_by_post_mid(post, mid)  # 由后序序列、中序序列构造二叉树
    T.pre_order_recursive(newT_post_mid)  # 获取前序序列
```

图的邻接表             

```python
n = 7
# 图的边数据
data = [
    [1, 0],
    [1, 2],
    [1, 3],
    [1, 6],
    [2, 0],
    [0, 6],
    [3, 6],
    [3, 4],
    [0, 5],
    [5, 6],
    [5, 3],
    [5, 4]
]

# 构建邻接表
n_node = 7
graph = [[] for _ in range(n_node)]
for edge in data:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
print(graph)
```