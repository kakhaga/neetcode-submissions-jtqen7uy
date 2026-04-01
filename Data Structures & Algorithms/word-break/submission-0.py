class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[-1] = True

        for itr in range(n-1, -1, -1):
            for word in wordDict:
                m = len(word)
                if (itr + m) <= n and s[itr : itr + m] == word:
                    dp[itr] = dp[itr + m]
                if dp[itr]:
                    break
        return dp[0]
