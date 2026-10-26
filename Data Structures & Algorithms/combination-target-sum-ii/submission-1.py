class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(start, path, remain):
            if remain == 0:
                result.append(path[:])


            if start >= len(candidates) or candidates[start] > remain:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])
                backtrack(i+1, path, remain-candidates[i])
                path.pop()
        
        backtrack(0, [], target)
        return result


        