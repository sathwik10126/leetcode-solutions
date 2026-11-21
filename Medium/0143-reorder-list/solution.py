# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
    
        temp = slow.next
        slow.next = None
        prev=None
        while temp:
            nxt=temp.next
            temp.next=prev
            prev=temp
            temp=nxt

      

        temp=head
        temp2=prev
        while temp2:
            t1=temp.next
            t2=temp2.next

            temp.next=temp2
            temp2.next=t1

            temp=t1
            temp2=t2


        
        
