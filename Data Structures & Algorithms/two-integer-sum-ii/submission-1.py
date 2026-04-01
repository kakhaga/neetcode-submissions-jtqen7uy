class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two sum but sorted
        # left to right and right to left while left < right
        left = 0
        right = len(numbers) - 1

        while left < right: # left = 0, right = 1
            currSum = numbers[left] + numbers[right]
            if currSum == target:
                return [left+1, right+1]
            elif currSum < target:
                left += 1
            else:
                right -= 1
        return []

