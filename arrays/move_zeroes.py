# Problem: Move Zeroes
# Link: https://leetcode.com/problems/move-zeroes/
#
# Approach:
#   Move the non-zero numbers to the front, keeping their order. Keep a marker
#   pos for the next free spot at the front. For each non-zero number, write it
#   at pos and move pos forward. After the loop, every spot from pos onwards
#   must be a zero, so fill them with 0. Everything is done in place.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        pos = 0
        for x in nums:
            if x != 0:
                nums[pos] = x
                pos += 1

        for i in range(pos, len(nums)):
            nums[i] = 0
