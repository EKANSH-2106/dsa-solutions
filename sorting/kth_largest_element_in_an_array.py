# Problem: Kth Largest Element in an Array
# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
#
# Approach:
#   Sort the array from largest to smallest. The kth largest element then sits
#   at position k - 1 (positions start at 0). Duplicates count as separate
#   elements, which matches the problem.
#   (A faster approach exists using a min-heap of size k, which runs in
#   O(n log k) and avoids sorting the whole array.)
#
# Time: O(n log n)
# Space: O(1) extra (the array is sorted in place)


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]
