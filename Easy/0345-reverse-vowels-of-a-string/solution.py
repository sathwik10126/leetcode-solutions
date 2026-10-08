class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        l=0
        r=len(s)-1
        while(l<r):
            if s[l].lower() in "aeiou":
                if s[r].lower() in "aeiou":
                    s[l],s[r]=s[r],s[l]
                    l+=1
                    r-=1
                else:
                    r-=1
            else:       
                l+=1
        return "".join(s)
