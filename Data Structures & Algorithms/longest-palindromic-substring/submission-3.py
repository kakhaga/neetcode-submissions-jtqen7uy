class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestLength = 0
        longestString = ''

        def isPalindrome(i,j):
            nonlocal longestString, longestLength
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j-i+1 > longestLength:
                    longestLength = j-i+1
                    longestString = s[i:j+1]
                i -= 1
                j += 1

        for i in range(len(s)):
            isPalindrome(i,i)
            isPalindrome(i,i+1)
        
        return longestString