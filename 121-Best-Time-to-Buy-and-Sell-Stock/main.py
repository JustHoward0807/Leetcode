class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Ideas
        #   Done this before using two pointers and track the max profit, but I want to learn sliding window method 
        # profit = 0
        # lowest = prices[0]

        # for i in range(1, len(prices)):
        #     if lowest > prices[i]:
        #         lowest = prices[i]
        #     else:
        #         profit = max(profit, prices[i] - lowest)

        # return profit

        # Sliding window (Figure out basically the same method from deepseek):
        left = 0
        profit = 0

        for right in range(1, len(prices)):
            if prices[left] > prices[right]:
                left = right # Here we basically saying move the left to lowest to buy
            else:
                profit = max(profit, prices[right] - prices[left])
        return profit