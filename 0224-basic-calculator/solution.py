class Solution:
    def calculate(self, s: str) -> int:
        exp = [ch for ch in s if ch != " "]

        def helper(i): # index
            num = 0
            res = 0
            sign = 1
            while i < len(exp):
                ch = exp[i]
                if ch.isdigit():
                    num = num * 10 + int(ch)
                elif ch == "+":
                    res += num *sign
                    num = 0
                    sign = 1
                elif ch == "-":
                    res += sign * num
                    num = 0
                    sign = -1
                elif ch == "(":
                    num, i = helper(i + 1)
                elif ch == ")":
                    res += sign * num
                    # finsihed a inner parenthesis so time to return
                    return res, i
                i += 1
            res += sign * num
            return res, i
        return helper(0)[0]

