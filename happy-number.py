#https://leetcode.com/problems/happy-number/


class Solution:
    def isHappy(self, n: int) -> bool:
        s=None
        h={}
        p={}
        check=0
        while True:
            sum=0
            for j in str(n):
                k=int(j)
                sum=sum+k**2
            #checking repetition for outputing False
            if sum not in p:
                    p[sum]=1
            elif sum in p:
                    check=check+1
                    print(check)
            if check==3:
                    print(p)
                    return False
            print(sum)
            n=sum
            if sum==1:
                return True
        
