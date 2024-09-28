# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        return self.dfs(n)

    def dfs(self, n):
        if n % 2 == 0:
            return []
        if n == 1:
            return [TreeNode(0)]
        res = []
        for i in range(1, n, 2):
            left_subtree = self.dfs(i)
            right_subtree = self.dfs(n - i - 1)
            for l in left_subtree:
                for r in right_subtree:
                    node = TreeNode(0, l, r)
                    res.append(node)
        return res
