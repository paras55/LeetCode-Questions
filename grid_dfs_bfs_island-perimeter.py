class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit=set()
        peri=0
        def dfs(i,j):
            if i >=len(grid) or j>=len(grid[0]) or i<0 or j<0 or grid[i][j]==0:
                return 1
            if (i,j) in visit:
                return 0
            
            visit.add((i,j))
            peri=dfs(i,j+1)
            peri=peri+dfs(i+1,j)
            peri=peri+dfs(i,j-1)
            peri=peri+dfs(i-1,j)
            
            return peri
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i,j)
                
        
        
        
        
        
        
        dfs(0,0)
        return peri
        
