class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = 1
        currMin = 1
        res = nums[0]

        for num in nums:
            tmp = currMax * num
            currMax = max(tmp, num*currMin, num)
            currMin = min(tmp, num*currMin, num)
            res = max(res, currMax)
        return res
        
        
        
        #     dp[i] = max(dp[i-1]*nums[i], nums[i])
        #     if dp[i] > output:
        #         output = dp[i]
        # return output