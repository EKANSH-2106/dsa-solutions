# Problem: Contains Duplicate
# Link: https://leetcode.com/problems/contains-duplicate/
#
# Approach:
#   Keep a set of numbers seen so far. For each number, if it is already in
#   the set, a duplicate exists, so return True. Otherwise add it and continue.
#   If the loop finishes with no repeat, return False.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False
