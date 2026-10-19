class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        pref = 1
        for i,num in enumerate(nums):
            res[i] = pref
            pref *= num
        suf = 1
        for i in range(n -1, -1, -1):
            res[i] *= suf
            suf *= nums[i]
        return res 
