class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1:
            return 0
        output = 0
        min_price = prices[0]

        for price in prices:
            min_price = min(min_price, price)
            output = max(output, price-min_price)
        
        return output

