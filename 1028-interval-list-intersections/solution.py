class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        m, n = len(firstList), len(secondList)
        i, j = 0, 0

        res = []

        while i < m and j < n:
            iterv1 = firstList[i]
            iterv2 = secondList[j]

            lo = max(iterv1[0],iterv2[0])
            hi = min(iterv1[1],iterv2[1])
            
            if lo <= hi:
                res.append([lo,hi])
            
            if iterv1[1] > iterv2[1]:
                j += 1
            else:
                i += 1
        return res 
            
