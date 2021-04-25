"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is not None:
            queue=[root]
            level=[]
            next_queue=[]
            result=[]
            while len(queue)>0:
                for root in queue:
                    level.append(root.val)
                    #print(root.children)
                    for hello in root.children:
                        next_queue.append(hello)
                print(level)
                result.append(level)
                level=[]
                queue=next_queue
                next_queue=[]

            return result
                    
