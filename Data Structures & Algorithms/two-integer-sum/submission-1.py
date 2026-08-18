class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            d[nums[i]] = i

        for i in range(len(nums)):
            y = target - nums[i]
            if y in d and d[y] != i:
                return [i, d[y]]
        