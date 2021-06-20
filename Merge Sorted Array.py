class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=0
        for j in range(len(nums1)):
            if nums1[j]==0:
                if i<=len(nums2)-1:
                    print(nums2[i])
                    nums1[j]=nums2[i]
                    i=i+1
        nums1.sort()
        
