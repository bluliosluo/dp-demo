from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums) - target
        if total % 2 or total < 0:
            return 0
        total //= 2
        dp = [0 for _ in range(total+1)]
        dp[0] = 1
        for num in nums:
            for i in range(total, -1, -1):
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[-1]

# Time: O(n*m)
# Space: O(n)


class Solution2:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        n = len(nums)
        if abs(target) > total_sum or (total_sum - abs(target)) % 2:
            return 0
        dp = [[0] * (total_sum * 2 + 1) for _ in range(n)]
        dp[0][total_sum + nums[0]] = 1
        dp[0][total_sum - nums[0]] += 1
        for i in range(1, n):
            for current_sum in range(2 * total_sum + 1):
                if dp[i-1][current_sum] > 0:
                    dp[i][current_sum - nums[i]] += dp[i-1][current_sum]
                    dp[i][current_sum + nums[i]] += dp[i-1][current_sum]

        return dp[n-1][target+total_sum]
