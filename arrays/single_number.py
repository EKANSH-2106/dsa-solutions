# Problem: Single Number
# Link: https://leetcode.com/problems/single-number/
#
# Approach:
#   Every number appears twice except one. Keep a set of numbers seen an odd
#   number of times: if a number is already in the set, its partner has
#   appeared, so remove it; otherwise add it. Pairs cancel out, and the one
#   number left in the set is the answer.
#   (An O(1) space version exists using XOR: x ^ x = 0 and x ^ 0 = x, so
#   XOR-ing all the numbers together leaves only the single one.)
#
# Time: O(n)
# Space: O(n)


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        seen = set()
        for x in nums:
            if x in seen:
                seen.remove(x)
            else:
                seen.add(x)
        return seen.pop()
