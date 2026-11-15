# Problem: Rotate Array
# Link: https://leetcode.com/problems/rotate-array/
#
# Approach:
#   Rotating right by k means the last k elements move to the front. Reduce k
#   with k % n first, since rotating by the length gives the same array. Then
#   rebuild the array as (last k elements) + (everything before them) using
#   slices, and assign it back with nums[:] so the change happens in place.
#   (An O(1) space version exists: reverse the whole array, then reverse the
#   first k elements and the remaining n - k elements separately.)
#
# Time: O(n)
# Space: O(n)  (the slices build a temporary list)


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]
