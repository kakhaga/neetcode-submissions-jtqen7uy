class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        allNums = set()
        for i in nums:
            allNums.add(i)

        maxCount = 0
        for i in nums:
            if i-1 not in allNums:
                curr = i
                count = 1
                while curr + 1 in allNums:
                    count += 1
                    curr += 1
                maxCount = max(maxCount, count)
        return maxCount