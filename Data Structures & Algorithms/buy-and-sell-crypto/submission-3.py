class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # minp = float('inf')
        # maxp = 0

        # for i, price in enumerate(prices):
        #     # set min profit to lowest
        #     if price < minp:
        #         minp = price
            
        #     # profit is price sold - min val
        #     currp = price - minp

        #     # to find max profit as highest
        #     if currp > maxp:
        #         maxp = currp
        
        # return maxp

        l , r = 0,1
        maxp = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                curp = prices[r]-prices[l]
                maxp = max(curp,maxp)
            else:
                l=r
            r+=1
        return maxp
