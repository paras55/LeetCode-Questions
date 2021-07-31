# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node,result):
            if node is None:
                return
            dfs(node.left,result)
            result.append(node.val)
            dfs(node.right,result)
            return result
        l=dfs(root,[])
        for i in range(len(l)-1):
            if l[i+1]<=l[i]:
                return False
        return True
        
        
           
