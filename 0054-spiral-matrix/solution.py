class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        m = len(matrix[0])
        top_row, bottom_row, left_col, right_col = 0, n - 1, 0, m - 1
        res = []
        while len(res) != m * n:
            # check first row
            for c in range(left_col, right_col + 1):
                res.append(matrix[top_row][c])
            top_row += 1
            
            for r in range(top_row, bottom_row + 1):
                res.append(matrix[r][right_col])
            right_col -=1

            if top_row <= bottom_row:
                for c in range(right_col, left_col -1, -1):
                    res.append(matrix[bottom_row][c])
                bottom_row -= 1
            if left_col <= right_col:
                for r in range(bottom_row, top_row - 1, -1):
                    res.append(matrix[r][left_col])
                left_col +=1
        return res 

