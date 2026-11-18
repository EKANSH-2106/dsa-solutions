# Problem: Two Sum II - Input Array Is Sorted
# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
#
# Approach:
#   Two pointers. The array is sorted, so put one marker at the start (left)
#   and one at the end (right) and add the two numbers. If the sum equals the
#   target, return the 1-based positions. If the sum is too small, move left
#   forward to get a bigger number. If it is too big, move right backward to
#   get a smaller one. Each step permanently discards one candidate, so one
#   pass is enough.
#   (A hash map like in Two Sum also works, but uses O(n) extra space.)
#
# Time: O(n)
# Space: O(1)


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1
