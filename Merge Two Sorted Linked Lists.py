# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#https://www.youtube.com/watch?v=OXmaACquVsY

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=ListNode()
        dummy=head
        
        while l1 and l2:
            if l1.val<l2.val:
                head.next=l1
                l1=l1.next
            else:
                head.next=l2
                l2=l2.next
            head=head.next
            
        if l1:
            head.next=l1
        if l2:
            head.next=l2
            
        return dummy.next #since head ke pehle node ko point karva rahe hain kyuki vo khud apne pehle node ko point ni kar sakta 
                
                    

        
        
