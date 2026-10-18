class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        left = 0
        curr = 0
        for i in range(n):
            while curr & nums[i] != 0:
                curr  ^= nums[left]
                left +=1
            curr ^= nums[i]
            res = max(res,i - left + 1)
        return res
