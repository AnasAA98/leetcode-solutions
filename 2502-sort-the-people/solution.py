class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        res = []
        for i in range(len(names)):
            res.append((heights[i], names[i]))
        res.sort(reverse = True)
        return [name for _,name in res]
