# Problem: Valid Palindrome II
# Link: https://leetcode.com/problems/valid-palindrome-ii/
#
# Approach:
#   Two pointers from both ends, moving inward while the characters match.
#   At the first mismatch we have exactly one deletion to spend, so there are
#   two options: skip the left character (check s[left+1..right]) or skip the
#   right character (check s[left..right-1]). If either remaining stretch is a
#   palindrome, the answer is True. A helper is_pal(l, r) checks whether the
#   part of s from l to r reads the same both ways.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_pal(left + 1, right) or is_pal(left, right - 1)
            left += 1
            right -= 1
        return True
