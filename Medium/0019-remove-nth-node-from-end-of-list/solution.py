# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        l=0
        temp=head
        while temp!=None:
            l+=1
            temp=temp.next
        i=0
        prev=None
        temp=head
        while(i<l-n and temp!=None):
            prev=temp
            temp=temp.next
            i+=1
        if prev==None:
            return head.next
        prev.next=temp.next
        
        return head
        
        
