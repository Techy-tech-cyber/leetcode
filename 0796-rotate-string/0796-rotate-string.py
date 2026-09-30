class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        n=len(s)
        if n!=len(goal):
            return False
        for i in range(0,n):
            if goal == s:
                return True
            s=s[-1]+s[:-1]
        return False        


                
       
