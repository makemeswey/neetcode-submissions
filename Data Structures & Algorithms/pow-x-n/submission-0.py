class Solution:
    def myPow(self, x: float, n: int) -> float:
        N = abs(n)
        current_product = x
        result = 1

        while N > 0:
            if N % 2 == 1:
                result *= current_product
            current_product *= current_product
            N //= 2

        return result if n >= 0 else 1 / result
        
        