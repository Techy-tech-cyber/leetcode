# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        def lvl(node):
            if node == None:
                return []
            res = []
            que = deque([node])
            ans = []

            while len(que) != 0:
                n = len(que)
                res = []

                for i in range(n):
                    e = que.popleft()
                    res.append(e.val)

                    if e.left is not None:
                        que.append(e.left)

                    if e.right is not None:
                        que.append(e.right)

                ans.append(res)

            return ans

        return lvl(root)         
       
            

        