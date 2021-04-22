# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.sum=0
        self.le=1
        self.ri=1
        self.heigh=0
    def height(self,root):  #height calculation of tree
        if root is None:
            return 0
        p=self.height(root.left)
        o=self.height(root.right)
        maxi=max(p,o)+1
        return maxi
    
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root is not None:
            print(root.val,self.ri)
            check=self.height(root)
            if check >self.heigh:
                self.heigh=check
            if root.left==None and root.right==None and (self.le==self.heigh or self.ri==self.heigh):
                self.sum=self.sum+root.val
            self.le=self.le+1
            
            l=self.deepestLeavesSum(root.left)
            self.le=0
            self.ri=self.ri+1
            r=self.deepestLeavesSum(root.right)
            return self.sum                                            
            
            
        
