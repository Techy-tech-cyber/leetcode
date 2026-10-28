class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
    
        res = [[1]]

        for i in range(rowIndex):
            temp = [0] + res[-1] + [0]
            c = []

            for j in range(len(res[-1]) + 1):
                c.append(temp[j] + temp[j + 1])

            res.append(c)

        return res[-1]