class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(path, start, remain):
            if remain == 0:
                result.append(path[:])
                return

            for i in range(start, len(nums)):
                if nums[i] > remain:
                    break

                path.append(nums[i])
                backtrack(path, i, remain - nums[i])
                path.pop()

        backtrack([], 0, target)
        return result

        