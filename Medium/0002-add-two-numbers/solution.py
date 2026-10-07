# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        r1=[]
        r2=[]
        def insert(data):
            nn=ListNode(data)
            if self.head==None:
                self.head=nn
            nn.next=head
            nn=head
        temp1=l1
        while temp1!=None:
            r1.append(temp1.val)
            temp1=temp1.next
        temp2=l2
        while temp2!=None:
            r2.append(temp2.val)
            temp2=temp2.next
        num1 = int(''.join(map(str, r1[::-1])))
        num2 = int(''.join(map(str, r2[::-1])))
        result = num1 + num2
        r = list(map(int, str(result)[::-1]))
        head=None
        temp=None
        for i in r:
            nn = ListNode(i)
            if head == None:
                head = nn
                temp = nn
            else:
                temp.next = nn
                temp = nn

        return head
        
