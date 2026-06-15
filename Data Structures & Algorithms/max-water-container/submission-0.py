class Solution:
    def maxArea(self, heights: List[int]) -> int:
        base = len(heights) - 1
        left = 0
        right = len(heights) - 1
        currheight = base * min(heights[left], heights[right])
        maxheight = base * min(heights[left], heights[right])
        while left < right:
            if heights[left] < heights[right]:
                left = left+1
                base -= 1
            elif heights[left] > heights[right]:
                right = right - 1
                base -=1
            else:
                left = left+1
                base -= 1
            currheight = base * min(heights[left], heights[right])
            maxheight = max(currheight, maxheight)
        return maxheight
