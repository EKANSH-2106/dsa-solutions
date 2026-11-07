# Problem: Running Sum of 1d Array
# Link: https://leetcode.com/problems/running-sum-of-1d-array/
#
# Approach:
#   The running sum at position i equals the running sum at position i - 1
#   plus the current number. So starting from position 1, add the previous
#   element to the current one, modifying the array in place.
#   (This is called a prefix sum.)
#
# Time: O(n)
# Space: O(1) extra (the array is modified in place)


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(1, n):
            nums[i] = nums[i - 1] + nums[i]
        return nums
