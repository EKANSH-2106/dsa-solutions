# Problem: Merge Intervals
# Link: https://leetcode.com/problems/merge-intervals/
#
# Approach:
#   Sort the intervals by their start, so any interval that overlaps with the
#   previous one comes right after it. Start the answer with the first
#   interval. For each next interval [start, end], compare it with the last
#   interval in the answer: if start <= that interval's end, they overlap (or
#   touch), so extend the last interval's end to max(old end, end). Otherwise
#   there is a gap, so append the new interval as it is.
#
# Time: O(n log n)  (sorting dominates; the loop is one pass)
# Space: O(n)  (the merged list, plus the sort's internal space)


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        return merged
