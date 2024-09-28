from typing import List


class Solution:
    def dfs(self, grid, i, j, left):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == -1:
            return
        if grid[i][j] == 2:
            if left == 0:
                self.res += 1
            return
        grid[i][j] = -1
        self.dfs(grid, i+1, j, left - 1)
        self.dfs(grid, i-1, j, left - 1)
        self.dfs(grid, i, j+1, left - 1)
        self.dfs(grid, i, j-1, left - 1)
        grid[i][j] = 0

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        count = sum(row.count(0) for row in grid)
        m = len(grid)
        n = len(grid[0])
        self.res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j, count + 1)
        return self.res
