class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for selling_price in prices:
            max_profit = max(max_profit, selling_price - min_price)
            min_price = min(min_price, selling_price)
        return max_profit
        