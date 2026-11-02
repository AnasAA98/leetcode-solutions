class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        res = 0
        curr = 0
        for dig in s:
            if int(dig) > k :
                return -1 
            curr = curr * 10 + int(dig)
            if curr > k:
                res += 1
                curr = int(dig)
        return res + 1


