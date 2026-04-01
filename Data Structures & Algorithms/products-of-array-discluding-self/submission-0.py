class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftMul = [1]*len(nums) # mul of all numbers on my left
        rightMul = [1]*len(nums) # mul of all numbers on my right

        # leftMul[0] = rightMul[len(nums)-1] = 1
        for i in range(1,len(nums)):
            leftMul[i] = leftMul[i-1] * nums[i-1]
        
        for i in range(len(nums) - 2, -1, -1):
            rightMul[i] = rightMul[i+1] * nums[i+1]
        
        out = [0] * len(nums)
        for i in range(len(nums)):
            out[i] = leftMul[i] * rightMul[i]
            
        return out
