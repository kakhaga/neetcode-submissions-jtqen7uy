class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            other = target - nums[i]
            if other in hashmap.keys():
                return [hashmap[other],i]
            hashmap[nums[i]] = i
        return []