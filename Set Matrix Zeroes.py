class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        l=[]
        if len(matrix)==0:
            return []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ele=matrix[i][j]
                s=[]
                if ele==0:
                    s.append(i)
                    s.append(j)
                    l.append(s)
                
        print (l)    
        for p in l:
            i=p[0]
            j=p[1]
            
            for e in range(len(matrix[0])):
                matrix[i][e]=0

            #column change
            for k in range(len(matrix)):

                matrix[k][j]=0
        
