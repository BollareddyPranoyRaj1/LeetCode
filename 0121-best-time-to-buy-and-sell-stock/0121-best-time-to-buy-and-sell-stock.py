class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        mini = float('inf')
        maxi = 0
        for i in range(len(prices)):
            if mini>prices[i]:
                mini=prices[i]
            maxi=max(maxi,prices[i]-mini)
        return maxi