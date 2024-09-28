from typing import List


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        res = 0
        dp = [0 for _ in range(len(s))]
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    if i >= 2:
                        dp[i] = dp[i-2] + 2
                    else:
                        dp[i] = 2
                elif i-dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
                    if i-dp[i-1] >= 2:
                        dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
                    else:
                        dp[i] = dp[i-1] + 2
                res = max(res, dp[i])
        return res
    
# Time: O(N)
# Space: O(N)
