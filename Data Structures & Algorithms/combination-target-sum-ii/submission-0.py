class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(path, start, remain):
            candidates.sort()

            if remain == 0:
                result.append(path[:])
                return 

            if start >= len(candidates) or remain < candidates[start]:
                return 

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(path, i+1, remain - candidates[i])
                path.pop()

        backtrack([],0,target)
        return result
        