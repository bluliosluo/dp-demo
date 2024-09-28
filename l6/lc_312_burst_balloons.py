from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # edge cases
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums)-2) + nums[0] ** 2 + nums[0]
        # dp represent the maximum coins we can get by bursting
        # the ballons from index i to index j

        # add the padding
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for left in range(n-2, 0, -1):
            for right in range(left, n-1):
                for i in range(left, right + 1):
                    gain = nums[left-1] * nums[i] * nums[right+1]
                    remain = dp[left][i-1] + dp[i+1][right]
                    dp[left][right] = max(dp[left][right], gain + remain)

        return dp[1][n-2]


class Solution2:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for length in range(3, n+1):
            for left in range(n - length + 1):
                right = left + length - 1
                for k in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right], dp[left][k] + nums[left] * nums[k] * nums[right] + dp[k][right])
        print(dp)
        return dp[0][n-1]
# Time: O(n^3)
# Space: O(n^2)