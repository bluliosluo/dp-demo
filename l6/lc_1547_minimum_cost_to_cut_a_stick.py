import sys
from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        n_cuts = len(cuts)
        
        # dp[i][j] represents the minimum cost to cut the stick from cuts[i] to cuts[j]
        dp = [[0 for _ in range(n_cuts)] for _ in range(n_cuts)]

        for length in range(2, n_cuts):
            for left in range(n_cuts - length):
                right = left + length
                dp[left][right] = sys.maxsize
                for mid in range(left + 1, right):
                    dp[left][right] = min(
                        dp[left][right], dp[left][mid] + dp[mid][right] + cuts[right] - cuts[left])

        return dp[0][n_cuts-1]

# Time: O(n^3)
# Space: O(n^2)