class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen :
                return False
            temp = 0
            seen.add(n)
            while n > 0:
                dig = n % 10
                temp += dig ** 2
                n = n // 10
            n = temp
        return True
