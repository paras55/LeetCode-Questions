#https://leetcode.com/problems/find-bottom-left-tree-value/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if root is not None:
            queue=[root]
            level=[]
            next_queue=[]
            result=[]
            #isme humne naya queue bna liya aur ek hi queme me bar bar nahi kara
            while len(queue)>0:
                for root in queue:
                    level.append(root.val)
                    if root.left is not None:
                        next_queue.append(root.left)
                    if root.right is not None:
                        next_queue.append(root.right)
                result.append(level)
                level=[]
                queue=next_queue
                next_queue=[]
            return result[-1][0]
        
