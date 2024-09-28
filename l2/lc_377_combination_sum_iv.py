from typing import List


class Solution:
    def dfs(self, nums, remain, memo):
        res = 0
        if remain < 0:
            return 0
        if remain == 0:
            return 1
        if memo[remain] != -1:
            return memo[remain]
        for num in nums:
            if num <= remain:
                res += self.dfs(nums, remain - num, memo)
        memo[remain] = res
        return res

    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = [-1 for _ in range(target+1)]
        return self.dfs(nums, target, memo)
# Time: O(n*m)


class Solution_DP:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[-1]
# Time: O(n*m)
