# Problem: Product of Array Except Self
# Link: https://leetcode.com/problems/product-of-array-except-self/
#
# Approach:
#   Brute force: for each position, multiply every other number (O(n^2),
#   gives Time Limit Exceeded).
#   Optimized: the answer at position i is (product of everything to the left
#   of i) * (product of everything to the right of i). Build a left list going
#   forwards (left[i] = left[i - 1] * nums[i - 1]) and a right list going
#   backwards (right[i] = right[i + 1] * nums[i + 1]), both starting at 1, then
#   multiply them position by position. No division is used.
#
# Time: O(n)
# Space: O(n)  (the left and right lists)


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left = [1] * n
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        right = [1] * n
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        answer = []
        for i in range(n):
            answer.append(left[i] * right[i])
        return answer
