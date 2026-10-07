class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        while "()" in s:
            s=s.replace("()","")
        return len(s)
