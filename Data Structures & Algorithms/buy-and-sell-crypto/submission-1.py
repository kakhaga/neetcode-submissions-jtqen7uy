class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy day i and a future sell day j
        # such that prices[j] - prices[i] is the maximum possible

        # brute force, start on everyday and seek the max value in future
        # Input: prices = [10,1,5,6,7,1]

        l, r = 0,1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP