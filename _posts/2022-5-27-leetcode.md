---
layout: post
title: leetcode
---
<!-- more -->
2. 两数之和                           

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums) - i -1):
                if nums[i] + nums[i + j + 1] == target:
                    return [i,i + j + 1]
```

104. 二叉树的最大深度                 

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    ending = 0
    def function(self,root,depth):
        print(root.val)
        if root.right != None:
            self.function(root.right, depth + 1)
        if root.left != None:
            self.function(root.left, depth + 1)
        if depth + 1 > self.ending:
            self.ending = depth + 1
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.function(root,0)
        return self.ending
```

102. 二叉树的层序遍历                       
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    ending = []
    def function(self, root, depth):
        depth += 1
        if len(self.ending) < depth:
            self.ending.append([])
            self.ending[depth - 1].append(root.val)
        else:
            self.ending[depth - 1].append(root.val)
        if root.left != None:
            self.function(root.left, depth)
        if root.right != None:
            self.function(root.right, depth)
            
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.ending = []
        if root:
            self.function(root,0)
            return self.ending
        else:
            return []
```

105. 从前序与中序遍历序列构造二叉树               

```python
'''
前序和中序顺序的结构：
前序 根节点 + 左子树 + 右子树
中序 左子树 + 根节点 + 右子树
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index + 1],inorder[:index])
        root.right = self.buildTree(preorder[index + 1:],inorder[index + 1:])
        return root
```

394. 字符串解码          

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
