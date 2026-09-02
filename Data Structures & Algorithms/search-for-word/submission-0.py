class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])

        def backtrack(r, c , k):
            if k == len(word):
                return True
            if (r < 0 or r >= row or c < 0 or c >= col or board[r][c] != word[k]):
                return False
            
            tmp = board[r][c]
            board[r][c] = "#"
            found = any(
                backtrack(r + dr, c + dc, k+1)
                for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]
            )

            board[r][c] = tmp
            return found

        return any(backtrack(r,c,0) for r in range(row) for c in range(col))
        