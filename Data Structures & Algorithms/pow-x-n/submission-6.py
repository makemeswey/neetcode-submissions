class Solution:
    def myPow(self, x: float, n: int) -> float:
        N = abs(n)
        result = 1
        curr_product = x

        while N > 0:
            if N & 1:
                result *= curr_product
            curr_product *= curr_product
            N >>= 1
        
        return result if n >= 0 else 1 / result