class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)

        if zero_count > 1:
            return [0] * len(nums)

        product = 1
        for num in nums:
            if num != 0:
                product *= num

        result = []

        for num in nums:
            if zero_count == 1:
                result.append(product if num == 0 else 0)
            else:
                result.append(product // num)

        return result