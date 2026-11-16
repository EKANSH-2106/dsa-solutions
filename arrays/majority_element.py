# Problem: Majority Element
# Link: https://leetcode.com/problems/majority-element/
#
# Approach:
#   Build a frequency dictionary (number -> count) while going through the
#   array. As soon as a number's count goes above n // 2, it is the majority
#   element, so return it.
#   (Shorter alternative: sort the array and return nums[n // 2], since the
#   majority element always covers the middle position.)
#
# Time: O(n)
# Space: O(n)


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = {}
        n = len(nums)
        for x in nums:
            count[x] = count.get(x, 0) + 1
            if count[x] > n // 2:
                return x
