class Solution:
    def isValid(self, s: str) -> bool:
        brc = {"(":")", "{":"}","[":"]"}
        stack = []
        for ch in s:
            if ch in brc:
                stack.append(ch)
            else:
                if not stack:
                    return False
                elif brc[stack[-1]] != ch:
                    return False
                stack.pop()
        return not stack
