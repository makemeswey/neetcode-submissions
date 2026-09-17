class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for idx, jump in enumerate(nums):
            if idx > max_reach:
                return False
            max_reach = max(max_reach, idx + jump)

        return True
        