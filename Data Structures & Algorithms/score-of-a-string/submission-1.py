class Solution:
    def scoreOfString(self, s: str) -> int:
        l = 0
        r = 1
        score = 0

        while r < len(s) and l < r:
            score += abs(ord(s[l]) - ord(s[r]))
            l = r
            r += 1

        return score

        