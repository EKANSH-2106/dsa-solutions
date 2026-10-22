# Problem: Valid Parentheses
# Link: https://leetcode.com/problems/valid-parentheses/
#
# Approach:
#   Use a stack. Push every opening bracket. When a closing bracket appears,
#   the most recent unclosed opener must match it, so pop the top of the stack
#   and compare it with the expected opener (looked up in a dictionary
#   closing -> opening). If the stack is empty or the types differ, return
#   False. After the loop, the string is valid only if the stack is empty
#   (no opener was left unclosed).
#
# Time: O(n)
# Space: O(n)


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack
