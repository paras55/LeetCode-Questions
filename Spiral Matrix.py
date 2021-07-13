#https://www.youtube.com/watch?v=pcPFrFK-ZVk

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)==0:
            return []
        row_begin=0
        row_end=len(matrix)
        column_begin=0
        column_end=len(matrix[0])
        size=len(matrix)*len(matrix[0])
        out=[]
        while row_begin < row_end and column_begin < column_end:
            #right
            for i in range(column_begin,column_end):
                out.append(matrix[row_begin][i])
            row_begin= row_begin+1
            if len(out)==size:
                break
            #down
            for j in range( row_begin,row_end):
                out.append(matrix[j][column_end-1])
            column_end=column_end-1
            if len(out)==size:
                break
            #left
            for k in range(column_end-1,column_begin-1,-1):
                out.append(matrix[row_end-1][k])
            row_end=row_end-1
            if len(out)==size:
                break
            #up
            for l in range(row_end-1,row_begin-1,-1):
                out.append(matrix[l][column_begin])
            column_begin=column_begin+1
            if len(out)==size:
                break
        return out
            
            
