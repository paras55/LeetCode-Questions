class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[]
        for j in range(1,numRows+1):
            l.append([1]*j)
        if numRows==0:
            return [[]]
        
        oldlist=[1,1]
        for p in l:
            if len(p)>2:
                no_of_changing_ele=(len(p)-2)+1
                print(no_of_changing_ele)
                for y in range(1,no_of_changing_ele):
                    print(y)
                    p[y]=oldlist[y-1]+oldlist[y]
                oldlist=p
        return l
                
