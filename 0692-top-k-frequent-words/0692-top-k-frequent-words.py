class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d={}
        for n in words:
            if n not in d:
                d[n]=1
            else:
                d[n]+=1
        
        A = sorted(d, key=lambda x: (-d[x], x))
        return A[:k]
        
        