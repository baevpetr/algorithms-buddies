from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode = None):
        self.val = val
        self.next = next


class AddTwoNumbers:
    """https://leetcode.com/problems/add-two-numbers/"""

    def iterating(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Time complexity: O(max(m, n))
        # Space complexity: O(max(m, n))

        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry

            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

    def recursion(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Time complexity: O(max(m, n))
        # Space complexity: O(max(m, n))

        def helper(l1: ListNode, l2: ListNode, carry) -> ListNode:
            if not l1 and not l2 and not carry:
                return None

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry

            carry = val // 10
            val = val % 10
            curr = ListNode(val)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr.next = helper(l1, l2, carry)

            return curr

        return helper(l1, l2, 0)
