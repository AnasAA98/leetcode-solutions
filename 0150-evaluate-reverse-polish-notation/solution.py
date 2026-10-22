class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        res = []
        ops = "+-*/"
        for ch in tokens:
            if ch in ops:
                num1 = int(res.pop())
                num2 = int(res.pop())
                if ch == "*":
                    res.append(str(num1 * num2))
                elif ch == "+":
                    res.append(str(num1 + num2))
                elif ch == "-":
                    res.append(str(num2 - num1))
                else:
                    res.append(str(int(num2 / num1)))
            else:
                res.append(ch)
        return int(res[0])



