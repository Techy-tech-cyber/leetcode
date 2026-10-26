# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def tra(node):
            if node == None :
                return 0
            LH=tra(node.left)
            RH=tra(node.right)
            if LH==-1 or RH==-1:
                return -1
            if abs(LH-RH)>1:
                return -1
            return 1+max(LH,RH)
        return tra(root)   !=-1     

        