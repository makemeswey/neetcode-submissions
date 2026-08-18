class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])

        def bfs(i, j):
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] != '1':
                return
            else:
                grid[i][j] = '0'
                bfs(i+1,j)
                bfs(i-1,j)
                bfs(i,j+1)
                bfs(i,j-1)

        num_islands = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    num_islands += 1
                    bfs(i, j)

        return num_islands

        