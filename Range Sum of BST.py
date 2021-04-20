# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sump=0
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
            if root is not None:
                if low<= root.val <=high :
                    self.sump=self.sump+root.val
                    print(self.sump)
                self.rangeSumBST(root.left,low,high)
                self.rangeSumBST(root.right,low,high)
        
        #helper(root,low,high)
            return self.sump
