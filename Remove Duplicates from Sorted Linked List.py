# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        itr=head
        while itr and itr.next:
            if itr.val==itr.next.val:
                itr.next=itr.next.next
                print(itr)
            else:   
                itr=itr.next
        return head
