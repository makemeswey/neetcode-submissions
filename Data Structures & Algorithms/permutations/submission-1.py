class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = set()

        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])

            for i in range(len(nums)):
                if i in used:
                    continue

                path.append(nums[i])
                used.add(i)

                backtrack(path)

                path.pop()
                used.remove(i)

        backtrack([])
        return result
        