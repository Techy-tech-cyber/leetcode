# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        temp1=headA
        temp2=headB
        c=0
        l=0
        while temp1!=None:
            temp1=temp1.next
            c+=1
        while temp2!=None:
            l+=1
            temp2=temp2.next
        dif=abs(c-l)
        if c>l:
            while dif:
                headA=headA.next 
                dif-=1
        else:
            while dif:
                headB=headB.next 
                dif-=1 
        while headA!=None:
            if headA==headB:
                return headA
            headA=headA.next
            headB=headB.next
        return None        


                
                    


