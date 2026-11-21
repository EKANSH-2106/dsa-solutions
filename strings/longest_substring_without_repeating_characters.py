# Problem: Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
# Approach:
#   Brute force: for each start i, extend j while keeping a set of the
#   characters seen, and stop at the first repeat (O(n^2)).
#   Optimized (sliding window): keep a window s[left..right] with no repeats,
#   tracked by a set. For each new character at right, while it is already in
#   the window, remove s[left] from the set and move left forward. Then add the
#   new character and update the best length with right - left + 1. Each
#   character enters and leaves the window at most once.
#
# Brute force: Time O(n^2), Space O(k)  (k = number of distinct characters)
# Sliding window: Time O(n), Space O(k)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        best = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            best = max(best, right - left + 1)
        return best


# Brute force version (kept for reference)
class SolutionBruteForce:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        for i in range(len(s)):
            seen = set()
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
                best = max(best, len(seen))
        return best
