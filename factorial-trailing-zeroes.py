# https://leetcode.com/problems/factorial-trailing-zeroes

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n==0:
            return 0
        fac=1
        for i  in range(1,n+1):
            fac=fac*i
        c=0
        while True:
            check=fac%10
            if check==0:
                c=c+1
                fac=fac//10
                continue
            else:
                break
        return c
            
            
