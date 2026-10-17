# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp=head
        c=0
        while temp!=None:
            c+=1
            temp=temp.next
    
        temp=head
        pos=0
        m=c//2
        if head.next==None:
            return None
        while temp!=None:
            if pos==m:
                prev.next=temp.next
            prev=temp
            temp=temp.next
            pos+=1
        return head
        
