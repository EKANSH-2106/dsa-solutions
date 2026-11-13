# Problem: Missing Number
# Link: https://leetcode.com/problems/missing-number/
#
# Approach:
#   The numbers 0 to n would add up to n * (n + 1) // 2 if none were missing.
#   The array adds up to that total minus the missing number, so the missing
#   number is the expected sum minus the actual sum of the array.
#   (A set also works: put nums in a set and return the first number from 0
#   to n that is not in it, using O(n) extra space.)
#
# Time: O(n)
# Space: O(1)


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2
        return expected - sum(nums)
