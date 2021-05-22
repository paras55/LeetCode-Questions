# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#https://leetcode.com/problems/middle-of-the-linked-list/

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        p=0
        itr=head
        while itr:
            p=p+1
            itr=itr.next
        
        count=p//2
        itr=head
        for i in range(count):
            itr=itr.next
        print(itr.next)
        return itr
        
