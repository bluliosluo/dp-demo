from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        for word in words:
            dp[word] = 1
        res = 1
        for word in sorted(words, key=len):
            for i in range(len(word)):
                pre = word[:i] + word[i+1:]
                if pre in dp:
                    dp[word] = max(dp[word], dp[pre] + 1)
                res = max(res, dp[word])
        return res

# Time: O(NlogN + N*W^2)
