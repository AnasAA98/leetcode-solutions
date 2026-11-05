class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        seen = set()

        def explore(r, c, index):
            if r < 0 or r >= row or c < 0 or c >= col or (r, c) in seen or board[r][c] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            seen.add((r,c))
            nxt = explore(r + 1, c, index + 1) or explore(r - 1, c, index + 1) or explore(r, c + 1, index + 1) or explore(r, c - 1, index + 1)
            seen.remove((r,c))
            return nxt
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and explore(i, j, 0):
                    return True
        
        return False
