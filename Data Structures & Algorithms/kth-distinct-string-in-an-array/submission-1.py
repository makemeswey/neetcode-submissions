class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}

        for ch in arr:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        unique = []
        for key, val in freq.items():
            if val == 1:
                unique.append(key)

        return unique[k-1] if len(unique) >= k else ""