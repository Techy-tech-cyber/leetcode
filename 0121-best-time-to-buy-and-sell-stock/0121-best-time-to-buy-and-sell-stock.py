class Solution(object):
    def maxProfit(self, p):
        """
        :type prices: List[int]
        :rtype: int
        """
        min=p[0]
        pro = 0
        for i in range (1,len(p)):
            if p[i]<min:
                min = p[i]
            if p[i] - min > pro:
                pro = p[i] - min

        return pro         

       
      
