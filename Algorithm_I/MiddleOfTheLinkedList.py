# Given the head of a singly linked list, return the middle node of the linked list.
#
# If there are two middle nodes, return the second middle node.
#
#
#
# Example 1:
#
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
#
# Example 2:
#
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Previously submitted Solution
# 60 ms, 13.7 MB
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        converted_list = []
        counter = 0
        while current_node != None:
            converted_list.append(current_node.val)
            current_node = current_node.next
        while counter < len(converted_list)//2:
            head = head.next
            counter += 1

        return head

# Solution by lee215
# https://leetcode.com/problems/middle-of-the-linked-list/discuss/154619/C%2B%2BJavaPython-Slow-and-Fast-Pointers

# Each time, slow go 1 steps while fast go 2 steps.
# When fast arrives at the end, slow will arrive right in the middle.

# C++:

    ListNode* middleNode(ListNode* head) {
        ListNode *slow = head, *fast = head;
        while (fast && fast->next)
            slow = slow->next, fast = fast->next->next;
        return slow;
    }

# Java:

    public ListNode middleNode(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

# Python:

    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
