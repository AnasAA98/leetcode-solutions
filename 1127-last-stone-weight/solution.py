class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        if len(heap) == 1:
            return -heap[0]
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            
            if x != y:
                we_diff = abs((-x) - (-y))
                heapq.heappush(heap,-we_diff)
        return -heap[0] if heap else 0
