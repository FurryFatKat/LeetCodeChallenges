# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.
#
#
#
# Example 1:
#
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
# Example 2:
#
# Input: list1 = [], list2 = []
# Output: []
#
# Example 3:
#
# Input: list1 = [], list2 = [0]
# Output: [0]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 991 ms, 14.3 MB
# this is an iterative approach
# this is a recursive question, not really solving this recursively
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == list2 and list1 is None:
            return list1
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        newNode = dummy = ListNode()
        print('list1: ', list1)
        print('list2: ',list2)
        while list1 and list2:
            if list1.val < list2.val:
                newNode.next = list1
                list1, newNode = list1.next, list1
            else:
                newNode.next = list2
                list2, newNode = list2.next, list2
            print('newNode: ', newNode)
            print('dummy: ', dummy)

        if list1 or list2:
            newNode.next = list1 if list1 else list2

        print(newNode)
        print(dummy)
        return dummy.next

# recursive solution from discussion board
# twice as fast: 463 ms, 14.2 MB

# https://leetcode.com/problems/merge-two-sorted-lists/discuss/9735/Python-solutions-(iteratively-recursively-iteratively-in-place).
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        print('list1: ', list1)
        print('list2: ', list2)
        if not list1 or not list2:
            return list1 or list2
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

'''

C++

https://leetcode.com/problems/merge-two-sorted-lists/discuss/1826666/C%2B%2B-oror-Easy-To-Understand-oror-2-Approaches-oror-Recursive-oror-Iterative

EXPLANATION

    Maintain a head and a tail pointer on the merged linked list.

    Then choose the head of the merged linked list by comparing the first node of both linked lists.

    For all subsequent nodes in both lists, you choose the smaller current node and link it to the tail of the merged list, and moving the current pointer of that list one step forward.

    You keep doing this while there are some remaining elements in both the lists.

    If there are still some elements in only one of the lists, you link this remaining list to the tail of the merged list.

    Initially, the merged linked list is NULL.

    Compare the value of the first two nodes and make the node with the smaller value the head node of the merged linked list.

    Since it’s the first and only node in the merged list, it will also be the tail.

    Then move head1 one step forward.

RECURSIVE APPROACH

					// 😉😉😉😉Please upvote if it helps 😉😉😉😉
class Solution {
public:
	ListNode* mergeTwoLists(ListNode* l1, ListNode* l2)
  {
		// if list1 happen to be NULL
		// we will simply return list2.
		if(l1 == NULL)
        {
			return l2;
		}

		// if list2 happen to be NULL
		// we will simply return list1.
		if(l2 == NULL)
        {
			return l1;
		}

		// if value pointend by l1 pointer is less than equal to value pointed by l2 pointer
		// we wall call recursively l1 -> next and whole l2 list.
		if(l1 -> val <= l2 -> val)
        {
			l1 -> next = mergeTwoLists(l1 -> next, l2);
			return l1;
		}
		// we will call recursive l1 whole list and l2 -> next
		else
        {
			l2 -> next = mergeTwoLists(l1, l2 -> next);
			return l2;
		}
	}
};

ITERATIVE APPROACH

					// 😉😉😉😉Please upvote if it helps 😉😉😉😉
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {

	    // if list1 happen to be NULL
		// we will simply return list2.
        if(list1 == NULL)
            return list2;

		// if list2 happen to be NULL
		// we will simply return list1.
        if(list2 == NULL)
            return list1;

        ListNode * ptr = list1;
        if(list1 -> val > list2 -> val)
        {
            ptr = list2;
            list2 = list2 -> next;
        }
        else
        {
            list1 = list1 -> next;
        }
        ListNode *curr = ptr;

		// till one of the list doesn't reaches NULL
        while(list1 &&  list2)
        {
            if(list1 -> val < list2 -> val){
                curr->next = list1;
                list1 = list1 -> next;
            }
            else{
                curr->next = list2;
                list2 = list2 -> next;
            }
            curr = curr -> next;

        }

		// adding remaining elements of bigger list.
        if(!list1)
            curr -> next = list2;
        else
            curr -> next = list1;

        return ptr;

    }
};



'''
