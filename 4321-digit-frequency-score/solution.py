class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        dig = [0] * 10
        n_str = str(n)

        for ch in n_str:
            dig[int(ch)] += 1
        res = 0
        for i in range(len(dig)):
            res += i * dig[i]
        
        return res 
