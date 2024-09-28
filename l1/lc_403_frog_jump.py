from collections import defaultdict
from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = defaultdict(set)
        dp[0].add(0)
        for s in stones:
            if s in dp:
                tmp = list(dp[s])
                for step in tmp:
                    for d in (-1, 0, 1):
                        dp[s + step + d].add(step+d)

        return len(dp[stones[-1]]) > 0
# Time: O(N^2)
# Space: O(N^2)
