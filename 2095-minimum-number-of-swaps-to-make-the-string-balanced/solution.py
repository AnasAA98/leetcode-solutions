class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        stack = []
        count = 0
        for ch in s:
            if ch == "[":
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
                    count += 2
        # count now stores number of valid bracktes
        k = (n - count) // 2
        return (k + 1) // 2
