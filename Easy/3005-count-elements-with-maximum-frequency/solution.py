class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        res=0
        for i in nums:
            d[i]=d.get(i,0)+1
        m=max(d.values())
        for i in d:
            if d[i]==m:
                res+=d[i]
        return res
