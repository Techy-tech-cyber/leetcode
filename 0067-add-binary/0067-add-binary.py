class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i=len(a)-1
        j=len(b)-1
        carry=0
        res=[]
        while i>=0 or j>=0 or carry:
            if i>=0:
                digit_a = int(a[i])
            else:
                digit_a = 0
            if j>=0:
                digit_b = int(b[j])
            else:
                digit_b = 0
            total = digit_a + digit_b + carry 
            res.append(str(total%2))
            carry = total//2
            i-=1
            j-=1
        res.reverse()
        return ''.join(res)    

        