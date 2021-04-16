# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        
        def helper(t1,t2):
            if t1 is None :
                return t2
            if t2 is None:
                return t1
            t1.val=t1.val+t2.val
            t1.left=helper(t1.left,t2.left)
            t1.right=helper(t1.right,t2.right)
                                     
            return t1
    
        o=helper(root1,root2)
        return o
            
        
        
