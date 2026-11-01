# Problem: Binary Search
# Link: https://leetcode.com/problems/binary-search/
#
# Approach:
#   Linear search: check every index from left to right (works, but slow).
#   Binary search: the array is sorted, so compare the target with the middle
#   element. If equal, return mid. If the middle is smaller than the target,
#   the target can only be in the right half (left = mid + 1). Otherwise it can
#   only be in the left half (right = mid - 1). Repeat while left <= right.
#   If the markers cross, the target is not present, so return -1.
#
# Linear search: Time O(n),     Space O(1)
# Binary search: Time O(log n), Space O(1)


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


# Linear search version (kept for reference)
class SolutionLinear:
    def search(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
