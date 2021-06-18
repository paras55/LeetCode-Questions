class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        h={}
        for ele in nums:
            if ele not in h:
                h[ele]=1
            else:
                h[ele]=h[ele]+1
        sum=0        
        for j in h:
            if h[j]==1:
                sum=sum+j
        return sum
    
        
