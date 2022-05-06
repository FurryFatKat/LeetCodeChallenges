# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # when we reach the end of the list nodes, next will have value of None
        # so we set that as the stop condition

        # we can put the characters into two strings
        # one in forward order
        # one in reverse order
        # and then compare them once the loop ends

        # to update the loop:
        # val will take on next.val
        # next will take on next.next
        current_val = head.val
        next_val = head.next
        forward = ''
        reverse = ''
        # This is the original code that ends one step too early
        # while next_val != None:
        #     forward += str(current_val)
        #     reverse = str(current_val) + reverse
        #     current_val = next_val.val
        #     next_val = next_val.next
        while True:
            try:
                forward += str(current_val)
                reverse = str(current_val) + reverse
                current_val = next_val.val
                next_val = next_val.next
            except:
                # use current_val error to break out of the loop
                break

        if forward == reverse:
            return true
        else:
            return false

        # this solution is really slow with 7345 ms of run time

        # # LeetCode solution to improve time and space complexity
        # vals = []
        # current_node = head
        # while current_node != None:
        #     vals.append(current_node.val)
        #     current_node = current_node.next
        # return vals == vals[::-1]
