from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = {}
        matched = 0
        required = len(need)

        for r in range(len(s2)):
            c = s2[r]
            window[c] = window.get(c,0) + 1

            if c in need and window[c] == need[c]:
                matched += 1

            l = r - len(s1)
            if l >= 0:
                d = s2[l]
                if d in need and window[d] == need[d]:
                    matched -= 1
                window[d] -= 1

            if matched == required:
                return True

        return False
        