# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l=0
        curr=head
        while curr!=None:
            l+=1
            curr=curr.next
        curr=head
        for i in range(l//2):
            curr=curr.next
        return curr        
        