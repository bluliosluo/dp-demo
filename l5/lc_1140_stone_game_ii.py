from typing import List
from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        for i in range(n - 2, -1, -1):
            piles[i] += piles[i + 1]

        @lru_cache(None)
        def dp(i, m):
            if i + 2 * m >= n:
                return piles[i]
            return piles[i] - min(dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))

        return dp(0, 1)



# Time: O(N^2)


# class Solution:
#     def stoneGameII(self, piles: List[int]) -> int:
#         n = len(piles)
#         dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
#         total_sum = [0 for _ in range(n+1)]

#         for i in range(n-1, -1, -1):
#             total_sum[i] = total_sum[i + 1] + piles[i]

#         for i in range(n-1, -1, -1):
#             for m in range(1, n+1):
#                 max_piles = min(n-i, 2*m)
#                 for x in range(1, max_piles+1):
#                     cur_sum = sum(piles[i:i+x])
#                     new_m = max(m, x)
#                     if x + i == n:
#                         dp[i][m] = max(dp[i][m], cur_sum)
#                     else:
#                         dp[i][m] = max(dp[i][m], cur_sum +
#                                        (total_sum[i] - cur_sum - dp[i+x][new_m]))
#         return dp[0][1]
