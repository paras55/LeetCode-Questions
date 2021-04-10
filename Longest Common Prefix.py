class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=[]
        if len(strs)==0:
            return ""
        
        for o in strs:
            if len(o)==0:
                return ""
            else:
               l.append(len(o))
        s=''   
        h={}
        mini=min(l)
        print(mini)
        for k in range(mini):
            h[k]=strs[0][k]
            print(h)
            for word in strs:
                letter=h[k]
                if letter != word[k]:
                    return s
                
            s=s+strs[0][k]
        
        return s
                    
