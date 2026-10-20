class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """

        result = []
        prev = 0

        for i in spaces:
            result.append(s[prev:i])
            prev = i

        result.append(s[prev:])

        return " ".join(result)
        
