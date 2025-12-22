class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        mini = float('inf')
        maxi = 0

        for i in range(len(prices)):
            mini = min(mini, prices[i])
            diff = prices[i] - mini
            maxi = max(maxi, diff)

        return maxi