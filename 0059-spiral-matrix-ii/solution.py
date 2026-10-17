class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]
        left, right, top, bottom = 0, n - 1, 0, n - 1
        count = 1
        while  count <= n ** 2:
            # top row
            for c in range(left, right + 1):
                matrix[top][c] = count
                count += 1
            top += 1
            # right col
            for r in range(top, bottom + 1):
                matrix[r][right] = count
                count+= 1
            right -= 1

            # bottom row
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    matrix[bottom][c] = count
                    count += 1
                bottom -= 1
            if left <= right:
                for r in range(bottom, top - 1, - 1):
                    matrix[r][left] = count
                    count += 1
                left += 1
        return matrix
