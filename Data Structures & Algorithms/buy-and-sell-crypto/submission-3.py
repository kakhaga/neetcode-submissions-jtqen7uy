class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not len(prices):
            return 0

        lowest = prices[0]  #7
        maxProfit = 0   #0

        for i in range(1,len(prices)):
            if prices[i] < lowest:  #1!<5
                lowest = prices[i]  # lowest = 1
            profit = prices[i] - lowest # profit = 0
            print(profit)
            if profit > maxProfit:
                maxProfit = profit  #maxProfit = 0
        return maxProfit