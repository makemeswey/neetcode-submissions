class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix[0]) * len(matrix) - 1
        while low <= high:
            mid = (low + high) // 2
            val = matrix[mid // len(matrix[0])][mid % (len(matrix[0]))]
            if val == target:
                return True
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
        