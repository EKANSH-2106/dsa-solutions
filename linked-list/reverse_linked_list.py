# Problem: Reverse Linked List
# Link: https://leetcode.com/problems/reverse-linked-list/
#
# Approach:
#   Walk through the list once while tracking three pointers: prev (starts as
#   None), curr (starts at head) and nxt. In each step: save the rest of the
#   list (nxt = curr.next), flip the arrow (curr.next = prev), then move prev
#   and curr one step forward. When curr becomes None, prev is the last node,
#   which is the new head of the reversed list.
#
# Time: O(n)
# Space: O(1)


# Definition for singly-linked list (provided by LeetCode).
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
