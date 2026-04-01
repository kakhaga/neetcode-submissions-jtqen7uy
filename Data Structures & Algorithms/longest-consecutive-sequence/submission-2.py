class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for num in nums:
            # not the start of a sequence
            if num-1 in numSet:
                continue
            # the start of the sequence
            length = 1
            while num+length in numSet:
                length += 1
            longest = max(longest, length)
        return longest
        