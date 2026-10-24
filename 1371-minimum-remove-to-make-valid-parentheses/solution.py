class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        inva = set() # will store indices to remove
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
                inva.add(i)
            elif s[i] == ')':
                if stack:
                    curr = stack.pop()
                    inva.remove(curr)
                else:
                    inva.add(i)
        res = []
        for i, ch in enumerate(s):
            if i in inva:
                continue
            else:
                res.append(ch)
        return "".join(res)
