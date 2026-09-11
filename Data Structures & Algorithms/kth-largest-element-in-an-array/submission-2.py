import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums = [-nums[n] for n in range(len(nums))]

        heapq.heapify(nums)

        for _ in range(k):
            result = -heapq.heappop(nums)

        return result
        