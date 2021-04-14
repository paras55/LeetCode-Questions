class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h={}
        for i in nums:
            if i not in h:
                h[i]=1
            else:
                h[i]=h[i]+1
        max=0
        ele=0
        for k in h:
            if h[k] >max:
                max=h[k]
                ele=k
        return ele
