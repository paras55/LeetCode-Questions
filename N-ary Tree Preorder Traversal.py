"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#children is a list of nodes 
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(node, result):
            if not node:
                return
            
            result.append(node.val)
            for child in node.children:
                print(type(child))
                dfs(child, result)
        
        result = []
        dfs(root, result)
        
        return result
