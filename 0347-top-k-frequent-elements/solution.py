class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        heap = []
        heapq.heapify(heap)
        for key,freq in count.items():
            heapq.heappush(heap,(freq,key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for _,num in heap]

