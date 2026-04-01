class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # slow pointer, fast pointer
        # set
        # maxLen

        left = 0
        lastSeenAt = {}
        res = 0

        for right in range(len(s)):
            if s[right] in lastSeenAt:
                left = max(left, lastSeenAt[s[right]] + 1)
            lastSeenAt[s[right]] = right
            res = max(res, right - left + 1)
        return res 


                