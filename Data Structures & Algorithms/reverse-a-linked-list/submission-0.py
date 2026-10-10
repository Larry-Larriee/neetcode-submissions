# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # given head of singly linked list meaning it has next node and value
        # goal of having the last node (the one with no next be the new head)
        # and the current head should be the tail
        
        # iterative solution
        current = head
        previous = None

        while current is not None:
            next = current.next # this is the temporary variable so we reverse the 
                                # current node while still being able to iterate

            current.next = previous
            previous = current
            current = next
        return previous # we can return previous because current.next ended up at
                        # a null pointer but previous is the last valid node
        
