class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,num in enumerate(nums):
            other = target - num
            if other in seen.keys():
                return [seen[other], i]
            seen[num] = i
        return []