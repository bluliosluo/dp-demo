from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        # dp[i] is the maximum sum we can get from arr[i:]
        dp = [0 for _ in range(n+1)]
        for start in range(n - 1, -1, -1):
            cur_max = 0
            for end in range(start, min(n, start + k)):
                cur_max = max(cur_max, arr[end])
                dp[start] = max(dp[start], cur_max *
                                (end - start + 1) + dp[end + 1])

        return dp[0]
# Time: O(N*K)