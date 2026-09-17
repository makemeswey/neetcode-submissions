class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum, best = nums[0], nums[0]

        for i in range(1, len(nums)):
            cur_sum = max(cur_sum + nums[i], nums[i])
            best = max(best, cur_sum)

        return best
        