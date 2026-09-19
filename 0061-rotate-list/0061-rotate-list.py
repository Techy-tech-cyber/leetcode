# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head == None or head.next==None:
            return head
        last=head
        c=0    
        while last.next!=None:
            last=last.next
            c+=1
        c+=1
        k=k%c
        if k==0 :
            return head
        curr=head
        for i in range(c-k-1):
            curr=curr.next
        last.next=head
        head=curr.next
        curr.next=None
        return head            
        
       