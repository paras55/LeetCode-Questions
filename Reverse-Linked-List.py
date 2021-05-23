# https://www.youtube.com/watch?v=XDO6I8jxHtA&t=293s
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev=None
        while head:
            temp=head
            head=head.next
            temp.next=prev
            prev=temp
        return prev
            
        
