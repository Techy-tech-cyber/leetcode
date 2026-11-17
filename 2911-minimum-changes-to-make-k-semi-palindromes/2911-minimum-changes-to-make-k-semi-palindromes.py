class Solution(object):
    def minimumChanges(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        cost = [[0] * n for _ in range(n)]

        # Precompute minimum changes
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                ans = float('inf')

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0
                    m = length // d

                    for r in range(d):
                        left = i + r
                        right = i + r + (m - 1) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    ans = min(ans, changes)

                cost[i][j] = ans

        # DP
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for p in range(1, k + 1):
                for j in range(i - 1):
                    if dp[j][p - 1] != float('inf'):
                        dp[i][p] = min(
                            dp[i][p],
                            dp[j][p - 1] + cost[j][i - 1]
                        )

        return dp[n][k]