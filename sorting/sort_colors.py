# Problem: Sort Colors
# Link: https://leetcode.com/problems/sort-colors/
#
# Approach:
#   Counting sort. The array only has the values 0, 1 and 2, so count how many
#   of each there are, then overwrite the array in place with that many 0s,
#   then 1s, then 2s.
#   (A one-pass, O(1) space version exists: the Dutch National Flag algorithm.)
#
# Time: O(n)
# Space: O(n)  (a temporary list is built before copying into nums)


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        zeros = nums.count(0)
        ones = nums.count(1)
        twos = nums.count(2)
        nums[:] = [0] * zeros + [1] * ones + [2] * twos
