# Problem: Intersection of Two Arrays
# Link: https://leetcode.com/problems/intersection-of-two-arrays/
#
# Approach:
#   Put the numbers of nums1 into a set for instant lookups. Go through nums2,
#   and whenever a number is in that set, add it to a result set (a set keeps
#   each number only once). Convert the result set to a list and return it.
#
# Time: O(n + m)
# Space: O(n + m)


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        result = set()
        for x in nums2:
            if x in set1:
                result.add(x)
        return list(result)
