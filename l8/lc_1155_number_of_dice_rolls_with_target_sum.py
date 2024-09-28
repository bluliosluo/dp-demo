from functools import cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 1000000007
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        # Initialize the base case
        dp[n][target] = 1

        for dice_index in range(n - 1, -1, -1):
            for curr_sum in range(target + 1):
                ways = 0

                # Iterate over the possible face values for the current die
                for i in range(1, min(k, target - curr_sum) + 1):
                    ways = (ways + dp[dice_index + 1][curr_sum + i]) % MOD

                dp[dice_index][curr_sum] = ways

        return dp[0][0]


class Solution2:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10 ** 9 + 7
        # dp[i][j]: i dices, sum to j, # possible ways
        if n * k < target:
            return 0

        @cache
        def dfs(i, j):
            # dfs(0, 0) = 1
            if j < 0:
                return 0
            if i == 0 and j == 0:
                return 1
            return sum(dfs(i-1, j-m) for m in range(1, min(k+1, j+1))) % mod
        return dfs(n, target)


class Solution3:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if not (n <= target <= n * k):
            return 0  # 无法组成 target
        MOD = 10 ** 9 + 7
        f = [[0] * (target - n + 1) for _ in range(n + 1)]
        f[0][0] = 1  # dfs(0, 0) = 1
        for i in range(1, n + 1):
            for j in range(target - n + 1):
                for x in range(min(k, j + 1)):  # 掷出了 x
                    f[i][j] = (f[i][j] + f[i - 1][j - x]) % MOD
        return f[n][-1]


class Solution4:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if not (n <= target <= n * k):
            return 0  # 无法组成 target
        MOD = 10 ** 9 + 7
        f = [1] + [0] * (target - n)
        for i in range(1, n + 1):
            max_j = min(i * (k - 1), target - n)  # i 个骰子至多掷出 i*(k-1)
            for j in range(1, max_j + 1):
                f[j] += f[j - 1]  # 原地计算 f 的前缀和
            for j in range(max_j, k - 1, -1):
                f[j] = (f[j] - f[j - k]) % MOD  # f[j] 是两个前缀和的差
        return f[-1]


