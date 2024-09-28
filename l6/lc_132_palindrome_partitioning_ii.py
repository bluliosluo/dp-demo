import sys


class Solution:
    def build_palindrome_table(self, s, n):
        res = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            res[i][i] = True
        for length in range(2, n+1):
            for i in range(n + 1 - length):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or res[i+1][j-1]:
                        res[i][j] = True
        return res

    def minCut(self, s: str) -> int:
        n = len(s)
        is_palindrome = self.build_palindrome_table(s, n)
        # dp[i] represents the nim cuts needed for the substring s[:i+1]
        dp = [sys.maxsize for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 0
        for i in range(2, n+1):
            for j in range(i):
                if is_palindrome[j][i-1]:
                    if j == 0:
                        dp[i] = 0
                    else:
                        dp[i] = min(dp[i], dp[j] + 1)
        return dp[n]

# Time: O(n^2)
# Space: O(n^2)