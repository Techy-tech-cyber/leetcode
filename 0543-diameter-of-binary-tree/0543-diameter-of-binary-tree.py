# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.D=0
        def tra (node):
            if node == None:
                return 0
            LH = tra(node.left)
            RH = tra(node.right)
            self.D=max(self.D,LH+RH)
            return 1+ max(RH,LH)
        tra(root)    
        return self.D        

        