class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        res = []
        heap = []
        for i,j in points:
            dist = math.sqrt((i**2) + (j**2))
            heapq.heappush(heap,(-dist,i,j))
            if len(heap) > k:
                heapq.heappop(heap)
        for _,x,y in heap:
            res.append([x,y])
        return res 


