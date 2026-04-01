class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # distance btw them right - left
        # height = min(left,right)
        maxArea = 0

        left, right = 0, len(heights) - 1
        while left < right:
            dist = right - left
            height = min(heights[left], heights[right])
            maxArea = max(maxArea, dist*height)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxArea