class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = -1 if (dividend < 0) != (divisor < 0) else 1

        a = abs(dividend)
        b = abs(divisor)

        ans = 0

        while a >= b:
            temp = b
            count = 1

            while a >= (temp << 1):
                temp = temp << 1
                count = count << 1

            a -= temp
            ans += count

        if sign == -1:
            ans = -ans

        return min(max(ans, -2**31), 2**31 - 1)
