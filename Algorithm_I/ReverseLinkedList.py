# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
#
#
# Example 1:
#
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
# Example 2:
#
# Input: head = [1,2]
# Output: [2,1]
#
# Example 3:
#
# Input: head = []
# Output: []

# I was only able to figure out iterative method within 20 minutes

# https://leetcode.com/problems/reverse-linked-list/discuss/58127/Python-Iterative-and-Recursive-Solution

class Solution:
# @param {ListNode} head
# @return {ListNode}
def reverseList(self, head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev

Recursion

class Solution:
# @param {ListNode} head
# @return {ListNode}
def reverseList(self, head):
    return self._reverse(head)

def _reverse(self, node, prev=None):
    if not node:
        return prev
    n = node.next
    node.next = prev
    return self._reverse(n, node)


'''
Java

https://leetcode.com/problems/reverse-linked-list/discuss/58125/In-place-iterative-and-recursive-Java-solution

public ListNode reverseList(ListNode head) {
    /* iterative solution */
    ListNode newHead = null;
    while (head != null) {
        ListNode next = head.next;
        head.next = newHead;
        newHead = head;
        head = next;
    }
    return newHead;
}

public ListNode reverseList(ListNode head) {
    /* recursive solution */
    return reverseListInt(head, null);
}

private ListNode reverseListInt(ListNode head, ListNode newHead) {
    if (head == null)
        return newHead;
    ListNode next = head.next;
    head.next = newHead;
    return reverseListInt(next, head);
}



'''



'''
C++

https://leetcode.com/problems/reverse-linked-list/discuss/58130/C%2B%2B-Iterative-and-Recursive

Well, since the head pointer may also be modified, we create a pre that points to it to facilitate the reverse process.

For the example list 1 -> 2 -> 3 -> 4 -> 5 in the problem statement, it will become 0 -> 1 -> 2 -> 3 -> 4 -> 5 (we init pre -> val to be 0). We also set a pointer cur to head. Then we keep inserting cur -> next after pre until cur becomes the last node. This idea uses three pointers (pre, cur and temp). You may implement it as follows.

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *pre = new ListNode(0), *cur = head;
        pre -> next = head;
        while (cur && cur -> next) {
            ListNode* temp = pre -> next;
            pre -> next = cur -> next;
            cur -> next = cur -> next -> next;
            pre -> next -> next = temp;
        }
        return pre -> next;
    }
};

Or

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *pre = new ListNode(0), *cur = head;
        pre -> next = head;
        while (cur && cur -> next) {
            ListNode* temp = cur -> next;
            cur -> next = temp -> next;
            temp -> next = pre -> next;
            pre -> next = temp;
        }
        return pre -> next;
    }
};

We can even use fewer pointers. The idea is to reverse one node at a time from the beginning of the list.

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* cur = NULL;
        while (head) {
            ListNode* next = head -> next;
            head -> next = cur;
            cur = head;
            head = next;
        }
        return cur;
    }
};

All the above solutions are iterative. A recursive one is as follows. First reverse all the nodes after head. Then we need to set head to be the final node in the reversed list. We simply set its next node in the original list (head -> next) to point to it and sets its next to NULL.

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head || !(head -> next)) {
            return head;
        }
        ListNode* node = reverseList(head -> next);
        head -> next -> next = head;
        head -> next = NULL;
        return node;
    }
};



'''




'''
C++ solution 2

https://leetcode.com/problems/reverse-linked-list/discuss/803955/C%2B%2B-Iterative-vs.-Recursive-Solutions-Compared-and-Explained-~99-Time-~85-Space

Not sure how this problem is expecting me to use less memory than this, but here is the deal:

    we are going to use 3 variables: prevNode, head and nextNode, that you can easily guess what are meant to represent as we go;
    we will initialise prevNode to NULL, while nextNode can stay empty;
    we are then going to loop until our current main iterator (head) is truthy (ie: not NULL), which would imply we reached the end of the list;
    during the iteration, we first of all update nextNode so that it acquires its namesake value, the one of the next node indeed: head->next;
    we then proceeding "reversing" head->next and assigning it the value of prevNode, while prevNode will become take the current value of head;
    finally, we update head with the value we stored in nextNode and go on with the loop until we can. After the loop, we return prevNode.

I know it is complex, but I find this gif from another platform to make the whole logic much easier to understand (bear in mind we do not need curr and will just use head in its place):

reverting a list

The code:

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *nextNode, *prevNode = NULL;
        while (head) {
            nextNode = head->next;
            head->next = prevNode;
            prevNode = head;
            head = nextNode;
        }
        return prevNode;
    }
};

Relatively trivial refactor (the function does basically the same) with recursion and comma operator to make it one-line:

class Solution {
public:
    ListNode* reverseList(ListNode *head, ListNode *nextNode = NULL, ListNode *prevNode = NULL) {
        return head ? reverseList(head->next, (head->next = prevNode, nextNode), head) : prevNode;
    }
};




'''
