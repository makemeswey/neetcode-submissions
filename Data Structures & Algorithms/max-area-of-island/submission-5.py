class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        max_area = 0

        def dfs(r,c):
            if r < 0 or r >= ROW or c < 0 or c >= COL or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            area = 1

            for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                area += dfs(r + dr, c + dc)

            return area

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))

        return max_area
        