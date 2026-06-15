class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxprice = 0
        while right < len(prices):
            currprice = prices[right] - prices[left]
            maxprice = max(currprice, maxprice)
            if prices[right] < prices[left]:
                left = right
                right = left + 1
            else:
                right = right + 1
        return maxprice
            