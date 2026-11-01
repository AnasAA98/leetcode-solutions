class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        n = len(nums)
        my_dict = defaultdict(int)
        for i in range(n):
            for j in nums[i]:
                my_dict[j] += 1
        res = []
        for key, val in my_dict.items():
            if val == n:
                res.append(key)
        res.sort()
        return res 
