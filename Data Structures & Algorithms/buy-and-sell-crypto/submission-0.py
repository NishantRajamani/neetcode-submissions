class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        for i in range(len(prices)-1):
            for j in range(i, len(prices)):
                newProfit = prices[j]-prices[i]
                if newProfit > profit:
                    profit = newProfit
        return profit