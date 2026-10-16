class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seq = set()
        left = 0
        res = 0
        for i in range(len(s)):
            while s[i] in seq:
                seq.remove(s[left])
                left += 1
            seq.add(s[i])
            res = max(res,len(seq))
        return res
