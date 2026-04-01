class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # product of the entire array
        # if even number of -ve numbers, all positive
        # if odd number of -ve numbers, all negative
        
        output = nums[0]
        for i in range(len(nums)):
            cur = nums[i]
            output = max(output, cur)
            for j in range(i+1,len(nums)):
                cur *= nums[j]
                output = max(output, cur)
        return output