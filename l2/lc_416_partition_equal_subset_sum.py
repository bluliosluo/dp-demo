from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2:
            return False
        target //= 2
        dp = [False for _ in range(target+1)]
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[-1]
# Time: O(n*m)
# Space: O(n)