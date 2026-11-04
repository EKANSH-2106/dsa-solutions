# Problem: Squares of a Sorted Array
# Link: https://leetcode.com/problems/squares-of-a-sorted-array/
#
# Approach:
#   Square every number in place, then sort the array. Squaring breaks the
#   original order (a large negative number becomes a large positive one),
#   so the sort is needed afterwards.
#   (A faster O(n) version exists using two pointers at the two ends, since
#   the largest square is always at one of the ends.)
#
# Time: O(n log n)  (O(n) for squaring, O(n log n) for sorting)
# Space: O(1) extra (the array is modified in place)


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(0, n):
            nums[i] **= 2
        nums.sort()
        return nums
