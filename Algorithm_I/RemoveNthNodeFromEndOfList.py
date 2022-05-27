# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
#
#
# Example 1:
#
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#
# Example 2:
#
# Input: head = [1], n = 1
# Output: []
#
# Example 3:
#
# Input: head = [1,2], n = 1
# Output: [1]


# I was not able to come up with my own solution in this case.
# Instead, I went to the discussion board to try and understand
# other people's methodologies.

# solution by StefanPochmann
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/8802/3-short-Python-solutions

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        for _ in range(n):
            # running through the steps
            fast = fast.next
        if not fast:
            # if fast is now None, return the next node
            return head.next
        while fast.next:
            # if not at the end of the linked list, keep counting
            fast = fast.next
            slow = slow.next
        # removing the value from next node
        slow.next = slow.next.next
        return head

# My first solution is "cheating" a little. Instead of really removing the nth node,
# I remove the nth value. I recursively determine the indexes (counting from back),
# then shift the values for all indexes larger than n, and then always drop the head.

class Solution:
    def removeNthFromEnd(self, head, n):
        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                node.next.val = node.val
            return i
        index(head)
        return head.next

Index and Remove - AC in 56 ms

# In this solution I recursively determine the indexes again,
# but this time my helper function removes the nth node. It returns two values.
# The index, as in my first solution, and the possibly changed head of the remaining list.

class Solution:
    def removeNthFromEnd(self, head, n):
        def remove(head):
            if not head:
                return 0, head
            i, head.next = remove(head.next)
            return i+1, (head, head.next)[i+1 == n]
        return remove(head)[1]
