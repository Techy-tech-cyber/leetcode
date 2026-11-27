class Solution(object):
    def convert(self, s, n):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        t = list (range(n))+ list(range(n-2,0,-1))
        r=['']*n
        for i ,char in enumerate(s):
            r[t[i%len(t)]]+=char
        return ''.join(r)     