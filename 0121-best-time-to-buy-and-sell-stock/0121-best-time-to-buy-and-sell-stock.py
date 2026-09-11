class Solution(object):
    def maxProfit(self, p):
        """
        :type prices: List[int]
        :rtype: int
        """
        low = p[0]
        maxProfit = 0
        for i in range (1,len(p)):
            if (low >p[i]):
                low=p[i]
            if( p[i]-low>maxProfit):
                maxProfit=p[i]-low
                
        return maxProfit      
