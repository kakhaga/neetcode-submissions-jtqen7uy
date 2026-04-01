class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            if i and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = n - 1
            
            while l < r:
                currSum = nums[i] + nums[l] + nums[r]
                if currSum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1] :
                        l += 1
                elif currSum < 0:
                    l += 1
                else: 
                    r -= 1
        return res