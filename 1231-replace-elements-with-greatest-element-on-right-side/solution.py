class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        n = len(arr)
        res = [-1] * n
        max_elm = -1
        for i in range(n -1, -1, -1):
            res[i] = max_elm
            max_elm = max(max_elm, arr[i])
        return res

