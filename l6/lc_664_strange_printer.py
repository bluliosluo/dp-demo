from typing import List


class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        # dp[i][j] represents the minimum number of turns to print s[i:j+1]
        dp = [[n] * n for _ in range(n)]
        for length in range(1, n+1):
            for left in range(n - length + 1):
                right = left + length - 1
                last_mismatched = -1
                for i in range(left, right):
                    if s[i] != s[right] and last_mismatched == -1:
                        last_mismatched = i
                    if last_mismatched != -1:
                        dp[left][right] = min(
                            dp[left][right], 1 + dp[last_mismatched][i] + dp[i+1][right])
                if last_mismatched == -1:
                    dp[left][right] = 0
        return dp[0][n-1] + 1
    
# Time: O(n^3)
# Space: O(n^2)
