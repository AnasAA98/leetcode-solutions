class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        res = 1
        left = 0
        for i in range(len(nums)):
            if nums[i] - nums[left] > k:
                res += 1
                left = i
        return res
