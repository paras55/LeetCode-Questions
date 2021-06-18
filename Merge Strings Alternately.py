class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=''
        print(word2[3:])
        n=min(len(word1),len(word2))
        for i in range(n):
            res=res+word1[i]
            res=res+word2[i]
        if len(word1) < len(word2):
            p=len(word1)
            res=res+word2[p:]
        elif len(word1) > len(word2):
            p=len(word2)
            res=res+word1[p:]
        return res
        
