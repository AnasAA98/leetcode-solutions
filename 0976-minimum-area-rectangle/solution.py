class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        min_area = math.inf
        cord = set()
        for x, y in points:
            cord.add((x,y))
        for x, y in cord:
            for px, py in cord:
                if (x, py) in cord and (px, y) in cord and x != px and y != py:
                    # we found a valid rectangle 
                    curr_area = abs(x - px) * abs(y - py) 
                    min_area = min(min_area, curr_area)
        return min_area if min_area != math.inf else 0
