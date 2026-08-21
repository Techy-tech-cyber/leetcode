class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        for n in nums:
            if n not in d:
                d[n]=1
            else:
                d[n]+=1
        
        A=sorted(d,key=d.get,reverse=True)
        return A[:k]
        