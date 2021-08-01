class Solution:
    def topView(self,root):
            val={}
            h=0
            queue=[[root,h]]
            while len(queue)>0:
                p=queue.pop(0)
                if p[1] not in val:
                    val[p[1]]=p[0].data
                if p[0].left is not None:
                    queue.append([p[0].left,p[1]-1])
                if p[0].right is not None:
                    queue.append([p[0].right,p[1]+1])
            l=[]
            for i in val:
                l.append(i)
            l.sort()
            p=[]
            for k in l:
                p.append(val[k])
            return p
