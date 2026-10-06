# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        def reverse(node,stop):
            prev = None
            curr = node
            while curr != stop:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        if left == right or not head:
            return head
        curr = head
        start_node, end_node = None, None
        count = 1
        while curr:
            if count + 1 == left:
                start_node = curr
            if count == right:
                end_node = curr.next
                break
            curr = curr.next
            count +=1
        if left == 1:
            new_head = reverse(head,end_node)
            head.next = end_node
            return new_head
        
        first = start_node.next
        start_node.next = reverse(first,end_node)
        first.next = end_node
        return head


        

         

        

