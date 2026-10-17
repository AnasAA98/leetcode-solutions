class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m, n = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, m - 1, 0, n - 1
        res = []
        while len(res) != m * n:
            # top row
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top +=1
            # right col
            for r in range(top,bottom + 1):
                res.append(matrix[r][right])
            right -= 1
            # bottom row
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1
        return res

