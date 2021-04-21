"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# https://www.youtube.com/watch?v=xdIjxF8zrVo&ab_channel=KashishMehndiratta



class Solution:
    def maxDepth(self, root: 'Node') -> int:
        max_depth = 0
        if root is None: 
            return 0
        for child in root.children:
            p=self.maxDepth(child)
            if p >max_depth:
                max_depth=p
        return max_depth + 1
        
        
        
