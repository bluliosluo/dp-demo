from typing import List


class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        currentState = list(currentState)
        if len(currentState) < 2:
            return []
        res = []
        for i in range(len(currentState) - 1):
            if currentState[i] != currentState[i + 1]:
                continue
            if currentState[i] == '+':
                currentState[i] = currentState[i + 1] = '-'
                res.append("".join(currentState))
                currentState[i] = currentState[i + 1] = '+'
        return res
