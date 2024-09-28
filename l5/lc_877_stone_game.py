from typing import List


# class Solution:
#     def stoneGame(self, piles: List[int]) -> bool:
#         n_piles = len(piles)
#         # initialize dp[i][j] which represents that maximum score difference
#         # the current player can achieve starting from piles[i] to piles[j]
#         dp = [[0] for _ in range(n_piles) for _ in range(n_piles)]
#         for i in range(n_piles):
#             dp[i][i] = piles[i]

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        # dp[i][j] represent the sum difference of the remaining piles from index i to index j
        dp = [[float('-inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]

        # dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        for length in range(1, n):
            for i in range(n - length):
                j = i + length
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])

        return dp[0][n-1] > 0
