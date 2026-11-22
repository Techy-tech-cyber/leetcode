class Solution(object):
    def intToRoman(self, n):
        """
        :type n: int
        :rtype: str
        """
        v=[
            1000,900,500,400,100,90,50,40,10,9,5,4,1
        ]
       
        s = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        R=[]
        
        for i in range (len(v)):
            while  n>=v[i] :
                
                R.append(s[i])
                n-=v[i]
        return "".join(R)       

        