class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts = Counter(nums)
        for i in nums:
            if (target - i) in nums and ((target - i) != i or counts[i] > 1):
                x = nums.index(i)
                y = nums.index(target - i,x+1)
                if x > y:
                    x, y = y, x
                return [x, y]
        return []
