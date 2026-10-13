class Solution:
    def myPow(self, x: float, n: int) -> float:
        N = abs(n)
        result = 1
        curr_prod = x

        while N > 0:
            if N % 2 == 1:
                result *= curr_prod
            curr_prod *= curr_prod
            N //= 2

        return result if n >= 0 else 1 / result
        