class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=1
        i=1
        d=1
        ans=1
        while(r<len(nums)):
            if nums[r] > nums[r - 1]:
                i += 1
                d = 1
            elif nums[r] < nums[r - 1]:
                d += 1
                i = 1
            else:
                i = 1
                d = 1
            ans = max(ans, i, d)
            r += 1

        return ans
        
