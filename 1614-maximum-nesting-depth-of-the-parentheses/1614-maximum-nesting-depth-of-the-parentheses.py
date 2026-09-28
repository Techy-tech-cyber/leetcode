class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        kela=0
        curr=0
        stack=[]
        for b in s:
            if b=="(":
                curr+=1
                stack.append(b)
                kela=max(kela,curr)
            elif(b==")"):
                curr-=1
                stack.pop()
        return kela            

        