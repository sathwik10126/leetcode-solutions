# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """ 
        r=[]
        temp1=list1
        temp2=list2
        while temp1:
            r.append(temp1.val)
            temp1 = temp1.next
        while temp2:
            r.append(temp2.val)
            temp2 = temp2.next
        r.sort(reverse=True)
        head=None
        for i in r:
            result=ListNode(i)
            if head==None:
                head=result
            else:
                result.next=head
                head=result
        return head


        
