class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches=0
        def odd(n):
            match=(n-1)//2
            return match
        def even(n):
            match=n//2
            return match
            
        while n>1:
            if n%2!=0:
                p=odd(n)
                matches=matches+p
                n=((n-1)//2)+1
            else:
                p=even(n)
                matches=matches+p
                n=n//2
        
        return matches
