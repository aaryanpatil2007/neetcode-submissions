class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxleft = 0
        maxright = 0
        waterlog = 0
        while left < right:
            if height[left] < height[right]:
                maxleft = max(maxleft, height[left])
                waterlog += maxleft - height[left]
                left += 1
            elif height[left] > height[right]:
                maxright = max(maxright, height[right])
                waterlog += maxright - height[right]
                right -= 1
            else:
                maxright = max(maxright, height[right])
                waterlog += maxright - height[right]
                right -= 1
        return waterlog
            
