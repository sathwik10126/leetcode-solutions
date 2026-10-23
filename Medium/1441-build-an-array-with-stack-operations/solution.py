class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        s=[]
        r=0
        for i in range(1,n+1):
            s.append("Push")
            if i==target[r]:
                r+=1
            else:
                s.append("Pop")
            if r==len(target):
                break
        return s
