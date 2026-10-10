class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = 0 # keep track of min value
        part = 0
        for i in range(len(nums)):
            if nums[i] - nums[left] > k:
                part += 1
                left = i
        return part + 1
