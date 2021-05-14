#https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays5135/1#

class Solution:
    def merge(self, arr1, arr2, n, m): 
        # code here
        arr2[:]=arr1+arr2
        arr2.sort()
        arr1[:]=arr2[0:n]
        arr2[:]=arr2[n:]
        #print(arr1+arr2)
        #print(arr2)
