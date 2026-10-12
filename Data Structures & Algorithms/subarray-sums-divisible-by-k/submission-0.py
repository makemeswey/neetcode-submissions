class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        seen = [0] * k
        seen[0] = 1

        cum_sum, count = 0, 0

        for num in nums:
            cum_sum = (cum_sum + num) % k
            count += seen[cum_sum]
            seen[cum_sum] += 1

        return count




        