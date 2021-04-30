# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        root1=root
        check=[root]
        root_list=[]
        l=[]
        def helper(root):       # this function is to create a list of values of BST 
            if root is not None:
                l.append(root.val)
                root_list.append(root)
                helper(root.left)
                helper(root.right)
        helper(root)
        h={}
        #print(check)
        for rot in root_list:   #this is to create a hashmap with updated values
            #print(rot)
            temp_sum=rot.val
            val=rot.val
            for j in l:
                if j>val:
                    temp_sum=temp_sum+j
            #print(temp_sum)
            h[rot.val]=temp_sum
        print(h)
              
        def helper2(root):      # this is to update the values in main root
            if root is not None:
                if root.val in h:
                    root.val=h[root.val]
                print(root.val)
                #print(root.left,root.right)
                helper2(root.left)
                helper2(root.right)
        helper2(root)
        return root
        #print(l)
