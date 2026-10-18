# Problem: Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/
#
# Approach:
#   Two strings are anagrams if they have the same letters with the same counts.
#   First, if the lengths differ, return False. Then build a frequency dictionary
#   (letter -> count) for each string and compare the two dictionaries.
#
# Time: O(n)
# Space: O(1) for lowercase letters (at most 26 keys), O(k) in general


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = {}
        for ch in s:
            count_s[ch] = count_s.get(ch, 0) + 1

        count_t = {}
        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1

        return count_s == count_t
