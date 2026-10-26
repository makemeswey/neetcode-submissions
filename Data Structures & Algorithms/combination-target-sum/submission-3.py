class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(start, path, remain):
            if remain == 0:
                result.append(path[:])
                return

            for i in range(start, len(nums)):
                if nums[i] > remain:
                    break
                
                path.append(nums[i])
                backtrack(i, path, remain - nums[i])
                path.pop()

        backtrack(0, [], target)
        return result
        