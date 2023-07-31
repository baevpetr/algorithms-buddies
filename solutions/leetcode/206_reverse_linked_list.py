from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode = None):
        self.val = val
        self.next = next


class ReverseLinkedList:
    def iterative(self, head: ListNode) -> ListNode:
        # Time complexity: O(n)
        # Space complexity: O(1)

        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next

        return prev

    def recursion(self, head: ListNode) -> ListNode:
        # Time complexity: O(n)
        # Space complexity: O(n)

        def helper(curr: ListNode, prev: ListNode = None) -> ListNode:
            if not curr:
                return prev

            next = curr.next
            curr.next = prev

            return helper(next, curr)

        return helper(head)

    def recursion_without_helper_1(self, head: ListNode) -> ListNode:
        # Time complexity: O(n)
        # Space complexity: O(n)

        if not head or not head.next:
            return head

        next = head.next
        head.next = None

        new_head = self.recursion_without_helper_1(next)
        next.next = head

        return new_head

    def recursion_without_helper_2(self, head: ListNode) -> ListNode:
        # Time complexity: O(n)
        # Space complexity: O(n)

        if not head:
            return None

        new_head = head
        if head.next:
            new_head = self.recursion_without_helper_2(head.next)
            head.next.next = head
            head.next = None

        return new_head
