"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        l=[]
        def order(node,l):
            if not node:
                return
            for i in node.children:
                order(i,l)
                l.append(i.val)
        order(root,l)
        if root is not None:
            l.append(root.val)
        return l
