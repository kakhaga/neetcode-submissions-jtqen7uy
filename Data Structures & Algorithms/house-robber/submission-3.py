class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        first = 0
        second = 0

        for num in nums:
            temp = max(first + num, second)
            first = second
            second = temp
        return second