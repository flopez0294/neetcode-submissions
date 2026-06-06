class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        low = prices[0]
        high = 0
        for idx, i in enumerate(prices[1:]):
            mx = max(i - low, mx)
            if low > i:
                low = i 
        return mx