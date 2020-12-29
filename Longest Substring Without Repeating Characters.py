class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        gl=0
        for i in range(len(s)): #outer loop
            track=''
            count=0
            h={}
            for j in range(i,len(s)):
                #print(j)
                if s[j] not in h:
                    h[s[j]]=1
                    #print(h)
                    track=track+s[j]
                    #print(track)
                    count=count+1
                    if count > gl:
                        gl=count
                    #print(count)
                else:
                        
                    break
                    
        print(gl)       
        return gl
