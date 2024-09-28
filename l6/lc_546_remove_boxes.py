from typing import List
from functools import cache


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:

        @cache
        def dp(i, j, k):
            if i > j:
                return 0
            while i < j and boxes[j] == boxes[j-1]:
                j -= 1
                k += 1

            if i == j:
                return (k+1)**2

            ans = (k+1)**2 + dp(i, j-1, 0)

            for m in range(j-1, i-1, -1):
                if boxes[m] == boxes[j]:
                    ans = max(ans, dp(i, m, k+1) + dp(m+1, j-1, 0))

            return ans

        return dp(0, len(boxes)-1, 0)
# Time: O(n^4)
# Space: O(n^3)


class Solution2:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        # dp[start][end][same_count] represent in the maximum points we can get by removing boxes from start to end assuming
        # there are same_count boxes adjacent to boxes[start] with the same color as boxes[start]
        dp = [[[0] * n for _ in range(n)] for _ in range(n)]

        # base case
        for end in range(n):
            for same_count in range(end + 1):
                dp[end][end][same_count] = (same_count + 1) * (same_count + 1)
        for length in range(1, n):
            for end in range(length, n):
                start = end - length
                for same_count in range(start + 1):
                    # try to merge start with all the same count before start
                    max_score = dp[start + 1][end][0] + \
                        (same_count + 1) * (same_count + 1)
                    for mid in range(start + 1, end + 1):
                        if boxes[mid] == boxes[start]:
                            max_score = max(
                                max_score, dp[start + 1][mid - 1][0] + dp[mid][end][same_count + 1])
                    dp[start][end][same_count] = max_score

        return dp[0][n-1][0]
# Time: O(n^4)
# Space: O(n^3)
