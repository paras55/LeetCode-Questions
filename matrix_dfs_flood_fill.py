class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        r=sr
        c=sc
        val=image[sr][sc]
        def dfs(r,c):
            if r<len(image) and c<len(image[1]) and r>=0 and c>=0:
                if image[r][c]==val:
                    image[r][c]=newColor
                    #top
                    dfs(r-1,c)
                    #bottom
                    dfs(r+1,c)
                    #left
                    dfs(r,c-1)
                    #right
                    dfs(r,c+1)
                    return image
                else:
                    return
            else:
                return
        
        if newColor==val:
            return image
        else:
            return dfs(r,c)
