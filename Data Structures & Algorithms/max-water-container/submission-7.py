class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, best = 0, len(heights) - 1, 0

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            best = max(best, area)

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1

        return best
        