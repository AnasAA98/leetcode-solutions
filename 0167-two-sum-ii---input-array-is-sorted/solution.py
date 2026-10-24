class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        left = 0
        right = n - 1
        while left <= right:
            curr = numbers[left] + numbers[right]
            if curr == target:
                return [left + 1, right + 1]
            if curr > target:
                right -= 1
            else :
                left += 1
        

