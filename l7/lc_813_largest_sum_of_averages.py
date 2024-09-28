from itertools import accumulate
from functools import cache
from typing import List


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix_sum = list(accumulate(nums, initial=0))

        @cache
        def dfs(i, j, m):
            if m == 1:
                return (prefix_sum[j+1] - prefix_sum[i]) / (j-i+1)

            res = 0
            for split in range(i, j):
                res = max(res, dfs(i, split, 1) + dfs(split + 1, j, m-1))
            return res

        return dfs(0, n-1, k)
# Time: O(N^2*K)
# Space: O(N*K)


class Solution2:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        # dp[i][j] split at j into i subarrays, max_score
        n = len(nums)
        dp = [[0.0 for _ in range(n)] for _ in range(k)]
        prefix = [0] + list(accumulate(nums))
        for i in range(n):
            dp[0][i] = (prefix[n] - prefix[i]) / (n-i)
        for k_index in range(1, k):
            for start in range(n):
                for end in range(start + 1, n):
                    dp[k_index][start] = max(
                        dp[k_index][start], dp[k_index-1][end] + (prefix[end] - prefix[start]) / (end - start))

        return dp[-1][0]
