class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxA = 0
        while left < right:
            area = min(heights[left], heights[right]) * (right-left)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            maxA = max(maxA, area)
        return maxA