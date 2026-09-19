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
        
        if head == None or head.next == None or k == 0:
            return head

        # length find karo
        temp = head
        n = 1

        while temp.next != None:
            temp = temp.next
            n += 1

        k = k % n

        if k == 0:
            return head

        # last node ko head se connect karo
        temp.next = head

        # new tail tak jao
        for i in range(n - k):
            temp = temp.next

        # new head
        new_head = temp.next

        # break the circle
        temp.next = None

        return new_head
    