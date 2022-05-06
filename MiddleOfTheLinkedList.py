# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
#
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        counter = 0
        while current_node != None:
            converted_list.append(current_node.val)
            current_node = current_node.next
        while counter < len(converted_list)//2:
            head = head.next
            counter += 1

        return head

# Initially, I had converted the ListNode to List for ease of operation and counting
# however, I run into the problem of having to convert List back to ListNode
# Looking through the discussion board, I found solution posted by felixplease
# it inspired me to use the length of floor divided list as counter to remove
# elements in head to get the second half of head
