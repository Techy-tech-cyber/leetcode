class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
    
        res = [[1]]

        for i in range(rowIndex):
            p=res[-1]
            temp = [0] + p + [0]
            c = []

            for j in range(len(p) + 1):
                c.append(temp[j] + temp[j + 1])

            res.append(c)

        return res[-1]