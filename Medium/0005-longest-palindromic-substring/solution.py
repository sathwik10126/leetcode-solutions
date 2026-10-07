class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=[]
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j]==s[i:j][::-1]:
                    res.append(s[i:j])
        return max(res,key=len)
        
