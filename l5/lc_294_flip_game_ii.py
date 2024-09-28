from functools import cache


class Solution:
    @cache
    def dfs(self, state):
        for i in range(len(state) - 1):
            if state[i:i+2] == "++":
                flipped_state = state[:i] + "--" + state[i+2:]
                if not self.dfs(flipped_state):
                    return True
        return False

    def canWin(self, currentState: str) -> bool:
        return self.dfs(currentState)
