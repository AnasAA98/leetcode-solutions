class DetectSquares:

    def __init__(self):
        self.cord = defaultdict(int)

    def add(self, point: list[int]) -> None:
        x, y = point
        self.cord[(x,y)] += 1
        

    def count(self, point: list[int]) -> int:
        res = 0
        x, y = point
        for px, py in self.cord:
            if abs(x - px) == abs(y - py) and (x, y) != (px,py):
                if (x,py) in self.cord and (px,y) in self.cord:
                    # found 4 valid points for a square
                    res += (self.cord[(px,py)] * self.cord[(x,py)] * self.cord[(px,y)]) 
        return res
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
