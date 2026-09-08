class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        r=0
        for i in range (len(nums)):
            left=total-r-nums[i]
            if left==r:
                return i
            r+=nums[i] 
        return -1       