# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res=[]
        def tra(node):
            if node == None:
                return 0
            res.append(node.val)
            tra(node.left)
            tra(node.right)
        tra(root)
        return res    



        