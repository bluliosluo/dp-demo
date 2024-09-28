# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, start, end):
        res = []
        if start > end:
            return [None]
        for i in range(start, end + 1):
            left_subtree = self.dfs(start, i - 1)
            right_subtree = self.dfs(i + 1, end)
            for l in left_subtree:
                for r in right_subtree:
                    node = TreeNode(i, l, r)
                    res.append(node)
        return res

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.dfs(1, n)
