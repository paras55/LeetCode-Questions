# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/problems/middle-of-the-linked-list/


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l=[]
        itr=head
        while itr:
            l.append(itr.val)
            itr=itr.next
        
        for i in range(len(l)):
            if l[i]!=l[len(l)-i-1]:
                return False
            
        return True
            
            
        
        
