class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        highest_freq = 0
        majority = 0
        for k, v in hashmap.items():
            if v > highest_freq:
                highest_freq = v
                majority = k

        return majority

        
        