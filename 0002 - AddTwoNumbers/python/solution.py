from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from listnode import ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        prev_node = None
        carry = 0
        while l1 is not None or l2 is not None:
            sum_val = carry
            if l1 is not None:
                sum_val += l1.val
                l1 = l1.next
            if l2 is not None:
                sum_val += l2.val
                l2 = l2.next
            current_node = ListNode(sum_val % 10)
            carry = sum_val // 10
            if prev_node is None:
                prev_node = current_node
                head = current_node
            else:
                prev_node.next = current_node
                prev_node = current_node
        if carry > 0:
            current_node.next = ListNode(carry)
        return head