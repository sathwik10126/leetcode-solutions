class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l=0
        r=0
        s=""
        while r<len(haystack):
            s+=haystack[r]
            if r-l+1==len(needle):
                if s==needle:
                    return l
                s=s[1:]
                l+=1
            r+=1
        return -1
            
