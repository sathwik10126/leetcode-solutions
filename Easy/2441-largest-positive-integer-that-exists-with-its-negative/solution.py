class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r=[]
        s=[]
        for i in nums:
            if i<0:
                r.append((-1)*i)
        for i in r:
            if i in nums:
                s.append(i)
        if s:
            return max(s)
        return -1


        
