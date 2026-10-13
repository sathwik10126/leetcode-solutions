class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        l=[]
        m=[]
        r=[]
        for i in nums:
            if i<pivot:
                l.append(i)
            elif i==pivot:
                m.append(i)
            else:
                r.append(i)
        return l+m+r
        
