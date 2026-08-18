from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        heap = []

        for key, val in freq.items():
            heapq.heappush(heap,(-val,key))

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        
        