class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        r=[0]*n
        i=0
        j=1
        for x in nums:
            if x<0:
                r[j]=x
                j+=2
            else:
                r[i]=x
                i+=2
        return r
