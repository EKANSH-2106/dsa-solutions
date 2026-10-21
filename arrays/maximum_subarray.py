# Problem: Maximum Subarray
# Link: https://leetcode.com/problems/maximum-subarray/
#
# Approach:
#   Brute force: for every start index i, extend the end index j while keeping
#   a running sum, and track the largest sum seen.
#   Optimized (one pass): at each number, track the best sum of a subarray that
#   ends at that number. Either extend the previous subarray (current + x) or
#   start fresh at x, whichever is larger. Track the best value seen overall.
#   Start both values at nums[0] so all-negative arrays are handled correctly.
#
# Brute force: Time O(n^2), Space O(1)  (gives Time Limit Exceeded on LeetCode)
# One pass:    Time O(n),   Space O(1)


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        best = nums[0]
        current = nums[0]
        for x in nums[1:]:
            current = max(x, current + x)
            best = max(best, current)
        return best


# Brute force version (kept for reference)
class SolutionBruteForce:
    def maxSubArray(self, nums: list[int]) -> int:
        best = nums[0]
        for i in range(len(nums)):
            current = 0
            for j in range(i, len(nums)):
                current = current + nums[j]
                best = max(best, current)
        return best
