class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        res = 0 
        n = len(difficulty)
        dif = [] # list of tuples (difficulty,profit)
        for i in range(n):
            dif.append((difficulty[i],profit[i]))
        dif.sort()
        worker.sort()
        res = 0
        left = 0
        best = 0
        for w in worker:
            while left < n and w >= dif[left][0]:
                best = max(best,dif[left][1])
                left += 1
            res += best
        return res
