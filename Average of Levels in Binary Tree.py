# https://www.youtube.com/watch?v=MBZ-gBkjdMc&ab_channel=DEEPTITALESRA

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[List[int]]:
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
            
            avg=[]
            for ele in result:
                no=len(ele)
                sum=0
                for i in ele:
                    sum=i+sum
                av=sum/no
                avg.append(av)
            return avg
            
                
                        
