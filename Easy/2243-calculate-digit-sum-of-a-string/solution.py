class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        while len(s)>k:
            r=""
            for i in range(0,len(s),k):
                g=(s[i:i+k])
                t= 0
                for j in g:
                    t+= int(j)
                r += str(t)
            s = r
        return s
