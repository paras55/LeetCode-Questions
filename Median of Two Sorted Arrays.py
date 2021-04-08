import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=[]
        med=0
        for i in nums1:
            l.append(i)
        for j in nums2:
            l.append(j)
        l.sort()
        print (l)
        no=len(l)
        print(no)
        if no%2 !=0:
            pos=math.ceil(no/2)
            print (pos)
            med=l[pos-1]
        else:
            pos=no//2
            med=(l[pos]+l[pos-1])/2
        return med
           
        
