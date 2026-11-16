class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            ans = ""

            for i in range(0, len(s), k):
                group = s[i:i+k]
                total = 0

                for j in group:
                    total += int(j)

                ans += str(total)

            s = ans

        return s
        