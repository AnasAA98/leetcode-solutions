class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        nums.sort()
        res = -1
        while right < len(nums):
            # min of window is left and max of window is right
            if nums[right] - nums[left] <= 2*k:
                res = max(res, right - left + 1)
                right += 1
            else:
                # if window too big then decrease the difference between nums[left] and nums[right]
                # new min in new nums[left]
                while nums[right] - nums[left] > 2 *k:
                    left += 1
        return res 


