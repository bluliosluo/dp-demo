import sys
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                cur = dungeon[i][j]
                # if right
                if j < n - 1:
                    health_needed_if_next_step_right = max(
                        1, dp[i][j + 1] - cur)
                else:
                    health_needed_if_next_step_right = sys.maxsize

                # if down
                if i < m - 1:
                    health_needed_if_next_step_down = max(
                        1, dp[i + 1][j] - cur)
                else:
                    health_needed_if_next_step_down = sys.maxsize

                dp[i][j] = min(health_needed_if_next_step_right,
                               health_needed_if_next_step_down)

                if i == m-1 and j == n-1:
                    dp[i][j] = 1 if dungeon[i][j] > 0 else 1 - cur

        return dp[0][0]
