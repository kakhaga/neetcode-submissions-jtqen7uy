class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestSize = 0
        longestIdx = 0

        def helper(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                nonlocal longestSize, longestIdx
                if longestSize < right - left + 1:
                    longestSize = right - left + 1
                    longestIdx = left
                left -= 1
                right += 1
            
        for i in range(len(s)):
            # case 1: odd length palindrome
            helper(i,i)
            # case 2: even length palindrome
            helper(i, i + 1)
        print(longestIdx, longestSize)
        return s[longestIdx: longestIdx + longestSize]

            
