# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        r=[]
        for l in lists:
            temp=l
            while(temp!=None):
                r.append(temp.val)
                temp=temp.next
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

