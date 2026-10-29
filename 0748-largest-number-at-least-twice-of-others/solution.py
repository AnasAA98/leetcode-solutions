class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        max_val = max(nums)
        res = nums.index(max_val)
        for i in range(len(nums)):
            if max_val != nums[i] and nums[i] * 2 > max_val:
                return -1
        
        return res
