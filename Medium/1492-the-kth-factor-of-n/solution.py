class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        r=[]
        for i in range(1,n+1):
            if n%i==0:
                r.append(i)
        r.sort()
        if len(r)<k:
            return -1
        else:
            return r[k-1]
