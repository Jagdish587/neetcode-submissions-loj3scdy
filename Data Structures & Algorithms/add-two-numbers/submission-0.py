# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        my_stack_1 = []
        my_stack_2 = []
        num_1 = 0
        num_2 = 0
        current_node_1 = l1
        current_node_2 = l2
        while current_node_1 != None:
            my_stack_1.append(current_node_1.val)
            current_node_1 = current_node_1.next


        while current_node_2 != None:
            my_stack_2.append(current_node_2.val)
            current_node_2 = current_node_2.next

        while my_stack_1:
            val = my_stack_1.pop()
            num_1 =  (num_1 * 10) + val

        while my_stack_2:
            val = my_stack_2.pop()
            num_2 =  (num_2 * 10) + val

        res = num_1 + num_2
        print("res  = ", res)

        res_head = None
        dummy_Node = ListNode(-1)
        dummy_Node.next = res_head
        if res == 0:
            self.addAtEnd(dummy_Node, 0)
        else:
            while res:
                digit = res % 10
                res = res // 10
                self.addAtEnd(dummy_Node, digit)
        
        return dummy_Node.next

    def addAtEnd(self, dummy_Node, val):
        new_node = ListNode(val)
        current_node = dummy_Node
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node