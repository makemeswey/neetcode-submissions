from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = Counter(magazine)

        for ch in ransomNote:
            if freq[ch] > 0:
                freq[ch] -= 1
            else:
                return False

        return True

        
        