from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for s in strs:
            count_zeros = s.count('0')
            count_ones = s.count('1')
            for i in range(m, count_zeros-1, -1):
                for j in range(n, count_ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-count_zeros]
                                   [j-count_ones] + 1)
        return dp[m][n]

# Time: O(n*m*len(strs))
# Space: O(n*m)
