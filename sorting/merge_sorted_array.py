# Problem: Merge Sorted Array
# Link: https://leetcode.com/problems/merge-sorted-array/
#
# Approach:
#   Overwrite the empty slots at the end of nums1 with nums2
#   (nums1[m:] = nums2), then sort nums1 in place.
#
# Time: O((m + n) log(m + n))
# Space: O(1) extra


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()
