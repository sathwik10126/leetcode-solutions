class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=0
        res=0
        while r<len(nums):
            if nums[r]==1:
                res=max(res,r-l+1)
                r+=1
            else:
                r+=1
                l=r
        return res
            
            
