# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        # dummy and tail act as the "aux" but it still uses the same ListNode
        # object instances

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1  # update tail value then move to next in tail
                list1 = list1.next # list1 is still preserved in the parameter
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        # we cant have an while with list1 or list2 because of our if conditional 
        # comparing 2 vals

        # the first while loop runs as long as both of the lists didn't hit
        # the end and this covers the case that one isn't exhausted yet
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        # we have dummy to avoid the edge case of a list with no nodes
        # and dummy.next returns the new head
        return dummy.next
