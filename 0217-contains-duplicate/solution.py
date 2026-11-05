class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = set(nums)
        return not len(res) == len(nums)
