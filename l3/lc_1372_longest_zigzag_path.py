# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def check(root, go_left, dist):
            if not root:
                return
            self.res = max(self.res, dist)
            if go_left:
                check(root.left, False, dist + 1)
                check(root.right, True, 1)
            else:
                check(root.left, False, 1)
                check(root.right, True, dist + 1)

        check(root, True, 0)
        check(root, False, 0)
        return self.res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def dfs(self, node, go_left, dist):
#         if not node:
#             return
#         self.res = max(self.res, dist)
#         if go_left:
#             self.dfs(node.left, False, dist + 1)
#             self.dfs(node.right, True, 1)
#         else:
#             self.dfs(node.left, False, 1)
#             self.dfs(node.right, True, dist + 1)

#     def longestZigZag(self, root: Optional[TreeNode]) -> int:
#         self.res = -sys.maxsize
#         self.dfs(root, False, 0)
#         return self.res
