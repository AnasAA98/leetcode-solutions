class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] >= x:
                right = mid
            else:
                left = mid + 1
        index = left
        left = index - 1
        right = index 
        count = 0
        while count != k:
            if left < 0:
                count += 1
                right += 1
            elif right > len(arr) - 1:
                left -= 1
                count +=1
            else:
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    left -= 1
                else:
                    right += 1
                count += 1
        return arr[left + 1: right ]            
   


