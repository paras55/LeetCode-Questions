#https://leetcode.com/problems/linked-list-cycle/



class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        h={}
        itr=head
        while itr:
            if itr.val not in h:
                h[itr.val]=1
            else:
                if h[itr.val]>1000:
                    return True
                h[itr.val]=h[itr.val]+1
            itr=itr.next
            
            
            
# Solutuon2 (preferred)

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        h={}
        itr=head
        while itr:
            if itr not in h:
                h[itr]=1
            else:
                return True
            itr=itr.next
        return False
            
