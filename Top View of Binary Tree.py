class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        
        queue=[{root:0}]
        level=[]
        h={}
        #queue.append()
        while len(queue)>0:
            dic=queue[0]
            for key, value in dic.items():
                root=key
                height=value
            #print(height)
            if root is not None:
                #print(root)
                if height not in h:
                    h[height]=[root.data]
                else:
                    h[height].append(root.data)
                    #h[height].sort()
                if root.left is not None:
                    queue.append({root.left:height-1})
                if root.right is not None:
                    queue.append({root.right:height+1})
                #print(queue)
            queue.pop(0)
        #print(h)
        k=[]
        for i in h:
            k.append(i)
        k.sort()
        final=[]
        for j in k:
            final.append(h[j])
        re=[]
        for res in final:
            re.append(res[0])
        return re
