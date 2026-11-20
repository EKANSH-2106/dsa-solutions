# Problem: 3Sum
# Link: https://leetcode.com/problems/3sum/
#
# Approach:
#   Sort the array, then fix the first number nums[i] with a loop. The other
#   two numbers must add up to -nums[i], and they lie to the right of i in a
#   sorted stretch, so this is Two Sum II: put left right after i and right at
#   the end, and move them inward based on whether the total is too small or
#   too big.
#   To avoid duplicate triplets (equal numbers sit next to each other after
#   sorting): skip nums[i] if it equals the number before it, and after finding
#   a triplet, move left forward past repeated values.
#   (Brute force with three loops is O(n^3) and far too slow.)
#
# Time: O(n^2)  (the outer loop times a two-pointer pass; sorting is O(n log n))
# Space: O(1) extra, not counting the result list


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result
