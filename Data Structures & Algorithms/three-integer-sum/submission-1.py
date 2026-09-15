class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            L, R = i + 1, len(nums) - 1
            while L < R:
                s = nums[i] + nums[L] + nums[R]
                if s == 0:
                    result.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1

                    while L < R and nums[L] == nums[L - 1]:
                        L += 1

                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1

                elif s < 0:
                    L += 1
                else:
                    R -= 1

        return result
        