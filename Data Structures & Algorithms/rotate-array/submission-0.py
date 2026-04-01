class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverseSubArray(l,r):
            nonlocal nums
            while l<r:
                nums[l], nums[r] = nums[r],nums[l]
                l += 1
                r -= 1


        if k > len(nums):
            k %= len(nums)
        
        nums.reverse()
        reverseSubArray(0,k-1)
        reverseSubArray(k,len(nums)-1)