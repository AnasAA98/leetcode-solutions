class Solution:
    def robotWithString(self, s: str) -> str:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        t = []
        p = []
        for ch in s:
            t.append(ch)
            count[ord(ch) - ord('a')] -= 1
            smallest_char = "{"
            for i in range(26):
                if count[i] > 0:
                    smallest_char = chr(ord('a') + i)
                    break
            while t and t[-1] <= smallest_char:
                p.append(t.pop())
        return "".join(p)            
