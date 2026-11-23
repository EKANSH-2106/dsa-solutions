# Problem: Top K Frequent Elements
# Link: https://leetcode.com/problems/top-k-frequent-elements/
#
# Approach:
#   Build a frequency dictionary (number -> count) in one pass. Then sort the
#   distinct numbers by their count, most frequent first, using
#   sorted(count, key=count.get, reverse=True), and return the first k.
#   (An O(n) version exists using bucket sort: put each number in a bucket
#   indexed by its count, then read the buckets from the highest count down.)
#
# Time: O(n log n)
# Space: O(n)


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1
        ordered = sorted(count, key=count.get, reverse=True)
        return ordered[:k]
