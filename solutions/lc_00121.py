# array

from typing import List

class Solution:    
    # The key is to find the minimum buying price.
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_buy_price = 0, prices[0]

        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_buy_price)
            min_buy_price = min(min_buy_price, prices[i])
        return max_profit
    
    # Gets TLE
    def maxProfit_v1(self, prices: List[int]) -> int:
        max_profit = 0

        for buy in range(len(prices)):
            for sell in range(buy + 1, len(prices)):
                max_profit = max(max_profit, prices[sell] - prices[buy])

        return max_profit


prices = [7,7,5,3,6,4]
solution = Solution()
max_profit = solution.maxProfit(prices)
print(max_profit)