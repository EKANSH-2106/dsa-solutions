# Problem: Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#
# Approach:
#   Brute force: try every (buy, sell) pair with sell after buy and keep the
#   max profit.
#   Optimized (one pass): walk through the days while tracking the cheapest
#   price seen so far. If today's price is lower, it becomes the new cheapest.
#   Otherwise, selling today earns (price - cheapest), so update the best
#   profit if that is larger. Best starts at 0 for the no-profit case.
#
# Brute force: Time O(n^2), Space O(1)  (gives Time Limit Exceeded on LeetCode)
# One pass:    Time O(n),   Space O(1)


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cheapest = prices[0]
        best = 0
        for price in prices:
            if price < cheapest:
                cheapest = price
            else:
                best = max(best, price - cheapest)
        return best


# Brute force version (kept for reference)
class SolutionBruteForce:
    def maxProfit(self, prices: list[int]) -> int:
        best = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                best = max(best, prices[j] - prices[i])
        return best
