# https://leetcode.com/problems/sum-of-left-leaves/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        l=[]
        self.sum=0
        def helper(root,flag):
            if root is not None:
                if flag==1:
                    if root.left is None and root.right is None:
                        self.sum=self.sum+root.val
                helper(root.left,1)
                helper(root.right,0)
        helper(root,0)
        return self.sum
