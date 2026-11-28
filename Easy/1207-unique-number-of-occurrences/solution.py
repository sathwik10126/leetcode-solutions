class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq={}
        l=[]
        for i in arr:
            freq[i]=freq.get(i,0)+1
        for i in freq:
            l.append(freq[i])
        if len(l)==len(set(l)):
            return True
        else:
            return False
