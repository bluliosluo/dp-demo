# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 0: not covered
# 1: covered
# 2: camera
# 00, 01, 02, 11, 12, 22


# 0: Strict ST; All nodes below this are covered, but not this one
# 1: Normal ST; All nodes below and incl this are covered - no camera
# 2: Placed camera; All nodes below this are covered, plus camera here


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node):
            if not node:
                return 1
            left = dfs(node.left)
            right = dfs(node.right)
            if left == 0 or right == 0:
                self.res += 1
                return 2
            if left == 1 and right == 1:
                return 0
            if left + right >= 3:
                return 1

        if dfs(root) == 0:
            self.res += 1
        return self.res
    

# class Solution:
#     def minCameraCover(self, root: Optional[TreeNode]) -> int:
#         def check(node):
#             if not node:
#                 return 0, 0, sys.maxsize
#             left = check(node.left)
#             right = check(node.right)
#             s0 = left[1] + right[1]
#             s1 = min(min(left[1:]) + right[2], min(right[1:]) + left[2])
#             s2 = 1 + min(left) + min(right)
#             return s0, s1, s2
#         return min(check(root)[1:])
