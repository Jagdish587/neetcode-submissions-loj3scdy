# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(-1)
        dummy_node.next = head
        left_node = dummy_node
        right_node = dummy_node
        for _ in range(n+1):
            right_node = right_node.next

        while right_node:
            right_node = right_node.next
            left_node = left_node.next

        left_node.next = left_node.next.next

        head = dummy_node.next
        return head