import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]

        heapq.heapify(nums)

        result = 0
        for i in range(k):
            result = -heapq.heappop(nums)

        return result

        