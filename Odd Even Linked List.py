# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#https://leetcode.com/problems/odd-even-linked-list/

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head
        oddptr=itr=head
        evenptr=abc=head.next
        i=1
        while itr:
            if i>2 and i%2 !=0:
                oddptr.next=itr
                oddptr=oddptr.next
            elif i>2 and i%2 ==0:
                evenptr.next=itr
                evenptr=evenptr.next
            itr=itr.next
            i=i+1
        evenptr.next=None
        oddptr.next=abc             #not  equal to evenptr because i have changed it 
        return head
        
        
