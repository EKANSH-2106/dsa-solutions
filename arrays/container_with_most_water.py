# Problem: Container With Most Water
# Link: https://leetcode.com/problems/container-with-most-water/
#
# Approach:
#   Two pointers. Start with the widest container (left at the start, right at
#   the end). The water held is min(height[left], height[right]) * (right - left),
#   since water spills over the shorter line. Track the best value seen. Then
#   move the marker at the shorter line inward: moving the taller one can never
#   help, because the width shrinks and the shorter line still limits the height.
#   (Brute force: try every pair, O(n^2), gives Time Limit Exceeded.)
#
# Time: O(n)
# Space: O(1)


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        best = 0
        while left < right:
            water = min(height[left], height[right]) * (right - left)
            best = max(best, water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best
