class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counter = {}
        majority = 0
        key = 0

        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1

        for k, v in counter.items():
            if v > majority:
                majority = v
                key = k

        return key

        
        