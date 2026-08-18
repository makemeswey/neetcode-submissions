from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = defaultdict(int)

        for ch in s:
            freq[ch] += 1

        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i

        return -1

        