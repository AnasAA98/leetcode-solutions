class ProductOfNumbers:

    def __init__(self):
        self.stack = [(1,1)] # stack of tuples

    def add(self, num: int) -> None:
        if num == 0:
            self.stack = [(1,1)]
        else:
            _,top = self.stack[-1]
            self.stack.append((num, top * num))

    def getProduct(self, k: int) -> int:
        n = len(self.stack)
        if k >= n:
            # going back to the last appearence of 0' in my window
            return 0
        return self.stack[-1][1] // self.stack[n - k - 1][1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
