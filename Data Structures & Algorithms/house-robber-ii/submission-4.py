class Solution:
    def rob(self, nums: List[int]) -> int:
        def hr(nums):
            rob1, rob2 = 0, 0
            for num in nums:
                rob1, rob2 = rob2, max(rob2, rob1+num)
            return rob2
        
        if len(nums) == 1:
            return nums[0]
        return max(hr(nums[1:]), hr(nums[:-1]))
