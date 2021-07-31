#User function Template for python3
https://www.youtube.com/watch?v=3MmWkR04n_8
'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

class Solution:
    #Function to return the lowest common ancestor in a Binary Tree.
    def lca(self,root, n1, n2):
        if root is None:
            return
        if root.data==n1 or root.data==n2:
            return root
        l=self.lca(root.left,n1,n2)
        r=self.lca(root.right,n1,n2)
        if l is not None and r is not None:
            return root
        if l is None:
            return r
        if r is None:
            return l
