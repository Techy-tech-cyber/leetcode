class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[[1]]
        for i in range (numRows -1 ):
            p=res[-1]
            temp= [0]+ p + [0]
            curr=[]
            for j in range (len(p) + 1):
                curr.append(temp[j]+temp[j+1])
            res.append(curr)
        return res          





               