class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums_combine = nums1 + nums2
        nums_combine.sort()

        n = len(nums_combine)

        if n % 2 == 1:
            return nums_combine[n // 2]
        else:
            mid = n // 2
            return (nums_combine[mid - 1] + nums_combine[mid]) / 2
                