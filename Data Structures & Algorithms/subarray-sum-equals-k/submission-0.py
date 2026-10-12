class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_counts = {0:1}
        current_sum, total_subarrays = 0, 0

        for num in nums:
            current_sum += num
            if (current_sum - k) in sum_counts:
                total_subarrays += sum_counts[current_sum - k]
            
            sum_counts[current_sum] = sum_counts.get(current_sum, 0) + 1

        return total_subarrays
        