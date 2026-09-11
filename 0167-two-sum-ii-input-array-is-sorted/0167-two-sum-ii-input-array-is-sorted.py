class Solution(object):
    def twoSum(self, n, t):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=0
        r=len(n)-1
        for i in range(len(n)):
            total=n[l]+n[r]
            if (total==t):
                return (l+1,r+1)
            elif (total>t) :
                r-=1
            else:
                l+=1       

                    
                