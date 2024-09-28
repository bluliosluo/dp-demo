from functools import cache
from itertools import accumulate
from typing import List

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        # dp[i][j][m]: min cost to merge stones from index i to index j (inclusive) into m piles
        # ans: dp[1][n][1]
        n = len(stones)
        # edge case
        if (n-1) % (k-1) != 0:
            return -1
        # prefix_sum
        prefix_sum = [0 for _ in range(n+1)]
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + stones[i]

        @cache
        def dfs(i, j):
            if j - i < k:
                return 0
            res = float('inf')
            for mid in range(i+1, j, k-1):
                res = min(res, dfs(i, mid) + dfs(mid, j))
            if (j-i-1) % (k-1) == 0:
                res += prefix_sum[j] - prefix_sum[i]
            return res
        return dfs(0, n)


class Solution2:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n-1) % (k-1) != 0:
            return -1
        prefix = [0] + list(accumulate(stones))
        # dfs(i, j, m) represents the min cost to merge stones[i:j+1] into m piles

        @cache
        def dfs(i, j, m):
            if i == j:
                return 0
            if m == 1:
                return (prefix[j+1] - prefix[i]) + dfs(i, j, k)
            ans = float('inf')
            for split in range(i, j, k-1):
                ans = min(ans, dfs(i, split, 1) + dfs(split+1, j, m-1))
            return ans
        return dfs(0, n-1, 1)



# Time: O(N^3)
# Space: O(N^2)
# # dp[i][j][m]: min cost to merge stones from index i to index j (inclusive) into m piles
#         # ans: dp[1][n][1]
#         n = len(stones)
#         # edge case
#         if (n-1) % (k-1) != 0:
#             return -1
#         # prefix_sum
#         prefix_sum = [0 for _ in range(n+1)]
#         for i in range(n):
#             prefix_sum[i+1] = prefix_sum[i] + stones[i]

#         # # base case:
#         # for i in range(n):

#         # return 0


