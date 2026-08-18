from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freq = Counter(nums)

        for number,count in freq.items():
            result.append((count,number))
            
        result.sort(reverse=True)
        return [num for count, num in result[:k]]

       

        