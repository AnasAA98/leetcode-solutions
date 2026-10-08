class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort() # sort by starting interval
        res = [intervals[0]]
        for intv in intervals[1:]:
            if res[-1][1] >= intv[0]:
                res[-1][1] = max(res[-1][1],intv[1])
            else:
                res.append(intv)
        return res 
