class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum, best = nums[0], nums[0]

        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            best = max(best, curr_sum)

        return best

        