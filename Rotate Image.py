#concept is to take the transpose and reverse the elements 
# https://www.youtube.com/watch?v=kd5u3GEQkPY


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                matrix[j][i] ,matrix[i][j] = matrix[i][j],matrix[j][i]
                
                
        for row in matrix:
            for i in range(len(row)//2):
                row[i],row[len(row)-i-1]=row[len(row)-i-1],row[i]

        
        
        
