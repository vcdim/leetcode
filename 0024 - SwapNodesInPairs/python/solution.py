from typing import Optional
from listnode import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        current_node = head
        next_node = current_node.next
        
        if next_node is not None:
            head = next_node
        prev_node = None
        
        while next_node is not None:
            # swap
            if prev_node is not None:
                prev_node.next = next_node
                
            current_node.next = next_node.next
            next_node.next = current_node
            
            # update
            prev_node = current_node
            if current_node.next is None:
                return head
            current_node = current_node.next
            if current_node.next is None:
                return head            
            next_node = current_node.next
            
        return head