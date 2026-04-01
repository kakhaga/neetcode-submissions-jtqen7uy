class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_helper(arr):
            left, right = 0,0
            
            for num in arr:
                temp = max(left + num, right)
                left = right
                right = temp
            return right
        
        if len(nums) < 3:
            return max(nums)
        return max(rob_helper(nums[1:]), rob_helper(nums[:-1]))