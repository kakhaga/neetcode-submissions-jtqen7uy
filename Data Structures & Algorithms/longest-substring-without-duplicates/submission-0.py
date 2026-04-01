class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        mp = {}
        output = 0

        for r in range(len(s)):
            if s[r] in mp.keys():
                l = max(l, mp[s[r]] + 1)
            mp[s[r]] = r
            output = max(output, r - l + 1)
        return output