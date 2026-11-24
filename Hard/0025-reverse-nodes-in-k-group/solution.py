# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        s=[]
        temp=head
        while temp:
            s.append(temp.val)
            temp=temp.next
        i=0
        j=k-1
        while j<len(s):
            l=i
            r=j
            while l<r:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
            i+=k
            j+=k
        temp=head
        while temp:
            temp.val=s.pop(0)
            temp=temp.next

        return head
        
        
