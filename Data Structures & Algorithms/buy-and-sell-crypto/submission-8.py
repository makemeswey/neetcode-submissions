class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, best = 0, 1, 0

        while l < r and r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                best = max(profit, best)
            else:
                l = r
            r += 1

        return best

        