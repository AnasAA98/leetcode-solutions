class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        n = len(nums)
        l = 0
        res = 0
        for r in range(n):
            if nums[r] != 1:
                res = max(res, r - l)
                l = r + 1
        return max(res, n - l)
            

