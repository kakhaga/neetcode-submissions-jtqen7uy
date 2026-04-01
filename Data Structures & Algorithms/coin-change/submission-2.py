class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        INF = amount + 1
        arr = [[INF for _ in range(amount+1)] for _ in range(n+1)]
        
        for i in range(n+1):
            arr[i][0] = 0
        
        for i in range(n-1, -1, -1):
            for a in range(1,amount+1):
                
                fromBelow = arr[i+1][a] # if i != n-1 else amount+1
                fromSameRow = 1+arr[i][a-coins[i]] if a-coins[i]>=0 else INF
                arr[i][a] = min(fromBelow, fromSameRow)
        return arr[0][amount] if arr[0][amount] != INF else -1
                