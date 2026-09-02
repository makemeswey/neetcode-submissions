class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(path, start):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                segment = s[start: end]
                if segment == segment[::-1]:
                    path.append(segment)
                    backtrack(path, end)
                    path.pop()

        backtrack([],0)
        return result