class Solution:
    def countSubstrings(self, s: str) -> int:
        
        output = 0
        if not s:
            return output

        def countPalindromes(i,j):
            nonlocal output
            if j >= len(s):
                return
            
            while i >= 0 and j < len(s) and s[i] == s[j]:
                output += 1
                i -= 1
                j += 1


        for i in range(len(s)):
            # odd length
            countPalindromes(i,i)

            # even length
            countPalindromes(i,i+1)
        
        return output

