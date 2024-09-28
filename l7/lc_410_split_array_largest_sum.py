from typing import List
import sys


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # dp[i][j] is the minimum largest sum we can get
        # from nums[i:] with j subarrays
        n = len(nums)
        dp = [[0 for _ in range(k + 1)] for _ in range(n)]

        prefix_sum = [0 for _ in range(n+1)]
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
        for subarray_count in range(1, k+1):
            for cur_idx in range(n):
                if subarray_count == 1:
                    dp[cur_idx][subarray_count] = prefix_sum[n] - \
                        prefix_sum[cur_idx]
                    continue
                min_largest_sum = sys.maxsize
                for split_idx in range(cur_idx, n - subarray_count + 1):
                    split_sum = prefix_sum[split_idx + 1] - prefix_sum[cur_idx]
                    largest_sum = max(
                        split_sum, dp[split_idx + 1][subarray_count - 1])
                    min_largest_sum = min(min_largest_sum, largest_sum)
                    if split_sum >= min_largest_sum:
                        break
                dp[cur_idx][subarray_count] = min_largest_sum
        return dp[0][k]

# Time: O(N^2*K)
# Space: O(N*K)