class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        for ch in strs :
            key=''.join(sorted(ch))
            if key not in d:
                d[key]=[]
            d[key].append(ch)
        return list(d.values())        

        
        