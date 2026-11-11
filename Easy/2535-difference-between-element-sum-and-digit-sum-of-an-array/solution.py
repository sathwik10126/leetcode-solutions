class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        e=sum(nums)
        s="".join(map(str, nums))
        r=0
        for i in s:
            r+=int(i)
        return abs(e-r)
