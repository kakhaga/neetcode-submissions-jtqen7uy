class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        i = 0
        j = len(nums) - 1

        while i < j:
            diff = target - nums[i] - nums[j]
            if diff == 0:
                return [i+1,j+1]
            elif diff > 0:
                i += 1
            else:
                j -= 1
        return []
            