# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        stack=[]
        res=[]
        curr=root
        while True:
            while curr:
                stack.append(curr)
                curr=curr.left
            if stack:
                pop=stack.pop()
                res.append(pop.val)
                curr=pop.right
            else:
                break
        return res                
        