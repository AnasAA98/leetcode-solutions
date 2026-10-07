class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        num = Counter(nums)
        dup =0
        for k in num:
            if num[k] > 1:
                    dup = k
        for i in range(1,len(nums) + 1):
            if i not in num:
                return[dup,i]


