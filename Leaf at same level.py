#User function Template for python3




class Solution:
    #Your task is to complete this function
    #function should return True/False or 1/0
    def check(self, root):
        l=[]
        def helper(root):
            if root is not None:
                if root.left is None and root.right is None:
                    l.append(root.data)
                helper(root.left)
                helper(root.right)
        def level(root):
            if root is not None:
                queue=[root]
                level=[]
                next_queue=[]
                result=[]
                #isme humne naya queue bna liya aur ek hi queme me bar bar nahi kara
                while len(queue)>0:
                    for root in queue:
                        level.append(root.data)
                        if root.left is not None:
                            next_queue.append(root.left)
                        if root.right is not None:
                            next_queue.append(root.right)
                    result.append(level)
                    level=[]
                    queue=next_queue
                    next_queue=[]
                return result
        helper(root)
        #print(l)
        ok=level(root)
        #print(ok)
        if ok[-1]==l:
            return True
        else:
            return False
            
