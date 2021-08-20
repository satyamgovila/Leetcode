# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## Iterative Solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev  = None
        current = head
        
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head  = prev
        return prev
    
   


## Recursive Solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse_helper(head)
    
    def reverse_helper(self , node , prev = None):
        if not node:
            return prev
        next = node.next
        node.next = prev
        
        return self.reverse_helper(next , node)
