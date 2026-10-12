# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        r=""
        temp=head
        while(temp!=None):
            r+=str(temp.val)
            temp=temp.next
        return int(r,2)
