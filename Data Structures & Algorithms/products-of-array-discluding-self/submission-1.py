class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftMul = [1] * n   #left to right
        rightMul = [1] * n  #right t left

        leftMul[0] = nums[0]
        for i in range(1,n):
            leftMul[i] = leftMul[i-1] * nums[i]

        rightMul[n-1] = nums[n-1]
        for i in range(n-2, 0, -1):
            rightMul[i] = rightMul[i+1] * nums[i]

        output = [1]*n
        output[0] = rightMul[1]
        output[n-1] = leftMul[n-2]
        for i in range(1,n-1):
            output[i] = leftMul[i-1]*rightMul[i+1]
        
        return output
            