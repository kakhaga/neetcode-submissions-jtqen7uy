class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resLen = 0
        n = len(s)
        
        def helper(l,r):
            nonlocal result, resLen
            while l >= 0 and r < n and s[l] == s[r]:
                if resLen < (r - l + 1):
                    result = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        for i in range(n):
            # odd length
            helper(i,i)

            # even length
            helper(i,i+1)
        
        return result