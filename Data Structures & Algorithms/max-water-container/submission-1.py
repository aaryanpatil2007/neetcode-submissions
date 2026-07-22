class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        totalmax = 0
        while left < right:
            base = right - left
            currmax = min(heights[left], heights[right]) * base
            totalmax = max(currmax, totalmax)
            if heights[left] <= heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
        return totalmax