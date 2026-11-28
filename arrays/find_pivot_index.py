# Problem: Find Pivot Index
# Link: https://leetcode.com/problems/find-pivot-index/
#
# Approach:
#   Compute the total sum of the array once. Walk through the array while
#   keeping a running left_sum (the sum of the numbers before the current
#   position). At each position i with number x, the sum on the right is
#   total - left_sum - x. If left_sum equals that, i is the pivot index, so
#   return it. Otherwise add x to left_sum and continue. If no position
#   balances, return -1.
#   (Simple version: for each i, sum nums[:i] and nums[i+1:], which is O(n^2).)
#
# Time: O(n)
# Space: O(1)


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i, x in enumerate(nums):
            right_sum = total - left_sum - x
            if left_sum == right_sum:
                return i
            left_sum += x
        return -1
