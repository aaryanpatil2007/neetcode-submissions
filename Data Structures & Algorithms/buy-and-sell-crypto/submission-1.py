class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        minimum = prices[0]
        currmax = 0
        for i in range(len(prices)):
            minimum = min(minimum, prices[i])
            currmax = max(prices[i] - minimum, currmax)
        return currmax
            
            