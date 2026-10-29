class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

    
        s1 = 0
        s2 = 0

        for money in nums:
            current = max(s1, s2 + money)
            s2 = s1
            s1 = current

        return s1

        