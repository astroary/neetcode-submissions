class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max, min

        minp = float("inf")
        maxp = 0

        for price in prices:
            if price < minp:
                minp = price
            maxp = max(maxp, price-minp)
        return maxp