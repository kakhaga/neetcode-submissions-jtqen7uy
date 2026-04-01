class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1
        while l< r:
            if s[l] != s[r]:
                return (self.isPalindrome(s,l+1,r) or self.isPalindrome(s,l,r-1))
            l += 1
            r -= 1
        return True

    #returns the indexes where they didnt match or -1,-1 if it is a palindrome.
    def isPalindrome(self, s, l, r):
        while l<r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
