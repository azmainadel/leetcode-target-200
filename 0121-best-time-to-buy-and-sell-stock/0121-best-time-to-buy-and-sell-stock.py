

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices) < 2):
            return 0
            
        minPrice = 999999
        maxProfit = 0

        for price in prices:
            minPrice = min(price, minPrice)
            maxProfit = max(maxProfit, price - minPrice)
        
        return maxProfit