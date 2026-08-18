class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set(nums)
        result = []

        for i in range(len(nums) + 1):
            if i not in seen:
                result.append(i)

        return result[0]


        