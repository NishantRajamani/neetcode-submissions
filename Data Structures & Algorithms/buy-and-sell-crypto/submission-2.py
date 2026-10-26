class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        sell = 1
        buy = 0
        while(sell<len(prices)):
            if prices[buy] > prices[sell]:
                print(prices[buy], prices[sell])
                buy = sell
                sell += 1
            else:
                newProfit = prices[sell]-prices[buy]
                profit = max(profit, newProfit)
                print(prices[buy], prices[sell])
                sell += 1
        return profit