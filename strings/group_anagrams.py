# Problem: Group Anagrams
# Link: https://leetcode.com/problems/group-anagrams/
#
# Approach:
#   Anagrams become identical when their letters are sorted, so the sorted
#   word works as a shared key. Use a dictionary mapping sorted-letters key ->
#   list of words. Append each word to the list for its key, then return all
#   the lists.
#
# Time: O(n * k log k)  (n words, k = max word length, sorting each word)
# Space: O(n * k)


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())
