from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        # for coin in coins:
        #     for i in range(coin, amount + 1):
        #         dp[i] = min(dp[i], dp[i-coin] + 1)

        for i in range(amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[-1] if dp[-1] != amount + 1 else -1
# Time: O(N*amount)
