# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
#
# Approach:
#   Brute force: check every pair (i, j) with j > i until nums[i] + nums[j] == target.
#   Optimized (hash map): for each number x, the partner we need is target - x.
#   Keep a dictionary of numbers already seen (value -> index). If the partner is
#   already in it, return both indices; otherwise store x and move on.
#
# Brute force: Time O(n^2), Space O(1)
# Hash map:    Time O(n),   Space O(n)


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # value -> index
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i


# Brute force version (kept for reference)
class SolutionBruteForce:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
