class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * m
        dp[0] = 1
        
        for i in range(n):
            for j in range(1,m):
                dp[j] += dp[j-1]
    
        return dp[-1]
