class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        h={}
        check=len(nums)//3
        for i in nums:
            if i not in h:
                h[i]=1
            else:
                h[i]=h[i]+1
                
        max=0
        ele=0
        l=[]
        for k in h:
            if h[k] >check:
                l.append(k)
        return l
