class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        count = 0

        def dfs(r,c):
            if r < 0 or r >= ROW or c < 0 or c >= COL or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                dfs(r + dr, c + dc)

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r,c)
        return count