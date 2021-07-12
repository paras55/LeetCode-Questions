class Solution:
    def Transpose(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                matrix[j][i] ,matrix[i][j] = matrix[i][j],matrix[j][i]
                
