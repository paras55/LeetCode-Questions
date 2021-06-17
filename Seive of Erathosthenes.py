#Seive of Erathosthenes - An algorithm to count prime numbers less than a given number


class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        l=[True]*n
        for i in range(2,n):
            for j in range(i*i,n,i):
                l[j]=False
        p=[] 
        for i in range(2,len(l)):
            if l[i]==True:
                p.append(i)
        return len(p)
        
