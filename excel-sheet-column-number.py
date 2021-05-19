#https://leetcode.com/problems/excel-sheet-column-number/


import string
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        h={}
        abc=str(string.printable[36:62])
        for i in range(1,27):
            h[abc[i-1]]=i
        print(h) # a dict of alphabets mapped to numbers
        col=0
        p=0
        for i in range(len(columnTitle)-1,-1,-1):
            col=col+h[columnTitle[i]]*(26**p)
            p=p+1
        return col
            
                    
                
            
