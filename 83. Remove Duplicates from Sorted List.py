# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# Easy
# Linked List

# TODO: przeanalizować to jeszcze raz
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        current = head
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head


delDuplicates = Solution()
# numbers = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
numbers = ListNode(0, ListNode(1, ListNode(2)))
delDuplicates.deleteDuplicates(numbers)
