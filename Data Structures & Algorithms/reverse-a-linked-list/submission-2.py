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
        
        # # iterative solution
        # current = head
        # previous = None

        # while current is not None:
        #     next = current.next # this is the temporary variable so we reverse the 
        #                         # current node while still being able to iterate

        #     current.next = previous
        #     previous = current
        #     current = next
        # return previous # we can return previous because current.next ended up at
        #                 # a null pointer but previous is the last valid node
        
        # O(n) time complexity as we're reversing and iterating linear to the size
        # of the linked list. 

        # O(1) space complexity of the algorithm (constant memory just 3 variables 
        # regardless of linked list size)

        # recursive solution:
        # the base case would be where current would hit null. But with recursion
        # you also break it down into subproblems meaning you grow your linked list
        # in reverse and each current for the subproblem will point to null

        if not head:
            return None # always start with the base case

        newHead = head # handles one node case and is how we go down subproblems
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head # this reverses the list so the next node now
        head.next = None          # points to you the current node
                                  # (imagine (head.next).next = head)

                                  # and our latest head is not the new end
        return newHead            # as it goes up the call stack it also saves 
                                  # the reverse head

        # O(n) time complexity (2n specifically since we go in and out of recursive
        # calls)

        # O(n) space complexity because we're making a living call stack even
        # if each subproblem layer is O(1) space complexity