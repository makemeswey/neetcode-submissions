from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)
        heap = []

        for n, f in freq.items():
            heapq.heappush(heap, (-f, n))

        result = []

        for _ in range(k):
            f, n = heapq.heappop(heap)
            result.append(n)

        return result