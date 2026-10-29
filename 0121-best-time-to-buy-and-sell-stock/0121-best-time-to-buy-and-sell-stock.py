class Solution(object):
    def maxProfit(self, p):
        """
        :type prices: List[int]
        :rtype: int
        """
      
        min_price = float('inf')
        profit = 0

        for p1 in p:
            min_price = min(min_price, p1)
            profit = max(profit, p1 - min_price)

        return profit
       
      
