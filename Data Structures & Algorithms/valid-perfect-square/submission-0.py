class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        L, R = 1, num

        while L <= R:
            M = (L + R) // 2
            M_squared = M * M

            if M_squared == num:
                return True
            elif M_squared < num:
                L = M + 1
            else:
                R = M - 1
        return False
        