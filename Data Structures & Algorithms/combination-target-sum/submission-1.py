class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(path, start, total):
            if total == target:
                result.append(path[:])
                return

            for i in range(start, len(nums)):
                if nums[i] + total > target:
                    break

                path.append(nums[i])
                backtrack(path, i, nums[i]+total)
                path.pop()

        backtrack([],0,0)
        return result


        