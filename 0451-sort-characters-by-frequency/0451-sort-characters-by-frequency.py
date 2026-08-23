class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        d={}
        for n in s:
            if n not in d:
                d[n]=1
            else:
                d[n]+=1
        
        A = sorted(d, key=d.get, reverse=True)
        ans = ""

        for ch in A:
            ans += ch * d[ch]

        return ans


        