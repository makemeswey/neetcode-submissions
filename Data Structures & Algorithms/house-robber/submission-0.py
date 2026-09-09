class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        memo = {}

        def dp(n):
            if n == 0:
                return 0
            if n == 1:
                return nums[0]

            
            if n in memo:
                return memo[n]

            skip = dp(n-1)
            take = dp(n-2) + nums[n-1]
            memo[n] = max(skip, take)

            return memo[n]
    
        return dp(len(nums))