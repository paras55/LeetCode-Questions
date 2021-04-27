# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        l=[]
        def helper(root):
            if root is not None:
                l.append(root.val)
                helper(root.left)
                helper(root.right)
        helper(root)
        for i in range(len(l)):
            target=k-l[0]
            l.remove(l[0])
            print(l)
            if target in l:
                return True
        return False
