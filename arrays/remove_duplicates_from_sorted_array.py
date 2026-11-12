# Problem: Remove Duplicates from Sorted Array
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#
# Approach:
#   The array is sorted, so duplicates sit next to each other. A number is new
#   exactly when it differs from the number just before it. Keep a counter k
#   (the next free spot at the front, which is also how many unique numbers
#   have been kept so far). For each new number, write it at position k and
#   move k forward. The first number is always unique, so k starts at 1 and the
#   loop starts at index 1. Return k.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k
