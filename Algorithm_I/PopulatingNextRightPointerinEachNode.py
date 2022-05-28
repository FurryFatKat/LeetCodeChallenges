# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
#
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
#
#
# Example 1:
#
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
#
# Example 2:
#
# Input: root = []
# Output: []

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# 108 ms, 15.8 MB
# using the failed method in Merge Two Binary Trees
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(x):
            left = x.left
            right = x.right
            if not left:
                return
            left.next = right
            if left.next and right.left:
                left.right.next = right.left
            if right.next and right.next.left:
                right.right.next = right.next.left
            [dfs(y) for y in (x.left, x.right)]

        if root:
            dfs(root)
            return root
        else:
            return


'''

https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/1654181/C%2B%2BPythonJava-Simple-Solution-w-Images-and-Explanation-or-BFS-%2B-DFS-%2B-O(1)-Optimized-BFS

✔️ Solution - I (BFS - Right to Left)

It's important to see that the given tree is a perfect binary tree. This means that each node will always have both children and only the last level of nodes will have no children.

Now, we need to populate next pointers of each node with nodes that occur to its immediate right on the same level. This can easily be done with BFS. Since for each node, we require the right node on the same level, we will perform a right-to-left BFS instead of the standard left-to-right BFS.

Before starting the traversal of each level, we would initialize a rightNode variable set to NULL. Then, since we are performing right-to-left BFS, we would be starting at rightmost node of each level. We set the next node of cur as rightNode and update rightNode = cur. This would ensure that each node would be assigned its rightNode properly while traversing from right to left.
Also, if cur has a child, we would first push its right child and only then its left child (since we are doing right-to-left BFS). Once BFS is completed (after queue becomes empty), all next node would be populated and we can finally return root.

The process is illustrated below -

C++

class Solution {
public:
    Node* connect(Node* root) {
        if(!root) return nullptr;
        queue<Node*> q;
        q.push(root);
        while(size(q)) {
            Node* rightNode = nullptr;                    // set rightNode to null initially
            for(int i = size(q); i; i--) {                // traversing each level
                auto cur = q.front(); q.pop();            // pop a node from current level and,
                cur -> next = rightNode;                  // set its next pointer to rightNode
                rightNode = cur;                          // update rightNode as cur for next iteration
                if(cur -> right)                          // if a child exists
                    q.push(cur -> right),                 // IMP: push right first to do right-to-left BFS
                    q.push(cur -> left);                  // then push left
            }
        }
        return root;
    }
};

Python

class Solution:
    def connect(self, root):
        if not root: return None
        q = deque([root])
        while q:
            rightNode = None
            for _ in range(len(q)):
                cur = q.popleft()
                cur.next, rightNode = rightNode, cur
                if cur.right:
                    q.extend([cur.right, cur.left])
        return root

Java

class Solution {
    public Node connect(Node root) {
        if(root == null) return null;
        Queue<Node> q = new LinkedList<>();
        q.offer(root);
        while(!q.isEmpty()) {
            Node rightNode = null;
            for(int i = q.size(); i > 0; i--) {
                Node cur = q.poll();
                cur.next = rightNode;
                rightNode = cur;
                if(cur.right != null) {
                    q.offer(cur.right);
                    q.offer(cur.left);
                }
            }
        }
        return root;
    }
}

Time Complexity : O(N), where N is the number of nodes in the given tree. We only traverse the tree once using BFS which requires O(N).
Space Complexity : O(W) = O(N), where W is the width of given tree. This is required to store the nodes in queue. Since the given tree is a perfect binary tree, its width is given as W = (N+1)/2 ≈ O(N)

✔️ Solution - II (DFS)

We can also populate the next pointers recursively using DFS. This is slightly different logic than above but relies on the fact that the given tree is a perfect binary tree.

In the above solution, we had access to right nodes since we traversed in level-order. But in DFS, once we go to the next level, we cant get access to right node. So, we must update next pointers of the child of each node from the its parent's level itself. Thus at each recursive call -

    If child node exists:

        assign next of left child node as right child node: root -> left -> next = root -> right. Note that, if once child exists, the other exists as well.
        assign next of right child node as left child of root's next (if root's next exists): root -> right -> next = root -> next -> left.
        How? We need right immediate node of right child. This wont exist if current root's next node doesnt exists. If next node of current root is present (the next pointer of root would already be populated in above level) , the right immediate node of root's right child must be root's next's left child because if child of root exists, then the child of root's next must also exist.

    If child node doesn't exist, we have reached the last level, we can directly return since there's no child nodes to populate their next pointers

The process is very similar to the one illustrated in the image below with just the difference that we are traversing with DFS instead of BFS shown below.

class Solution {
public:
    Node* connect(Node* root) {
        if(!root) return nullptr;
        auto L = root -> left, R = root -> right, N = root -> next;
        if(L) {
            L -> next = R;                                // next of root's left is assigned as root's right
            if(N) R -> next = N -> left;                  // next of root's right is assigned as root's next's left (if root's next exist)
            connect(L);                                   // recurse left  - simple DFS
            connect(R);                                   // recurse right
        }
        return root;
    }
};

Python

class Solution:
    def connect(self, root):
        if not root: return None
        L, R, N = root.left, root.right, root.next
        if L:
            L.next = R
            if N: R.next = N.left
            self.connect(L)
            self.connect(R)
        return root

Java

class Solution {
    public Node connect(Node root) {
        if(root == null) return null;
        Node L = root.left, R = root.right, N = root.next;
        if(L != null) {
            L.next = R;
            if(N != null) R.next = N.left;
            connect(L);
            connect(R);
        }
        return root;
    }
}

Time Complexity : O(N), each node is only traversed once
Space Complexity : O(logN), required for recursive stack. The maximum depth of recursion is equal to the height of tree which in this case of perfect binary tree is equal to O(logN)

✔️ Solution - III (BFS - Space-Optimized Appraoch)

This is a combination of logic of above logics- we will traverse in BFS manner but populate the next pointers of bottom level just as we did in the DFS solution.

Usually standard DFS/BFS takes O(N) space, but since we are given the next pointers in each node, we can use them to space-optimize our traversal to O(1).

    We first populate the next pointers of child nodes of current level. This makes it possible to traverse the next level without using a queue. To populate next pointers of child, the exact same logic as above is used
    We simply traverse to root's left child and repeat the process - traverse current level, fill next pointers of child nodes and then again update root = root -> left. So, we are basically performing standard BFS traversal in O(1) space by using next pointers to our advantage
    The process continues till we reach the last level of tree

The process is illustrated in images below -

Image 	Description
	We start with a perfect binary tree with all next pointers initially NULL
	We start traversal level-by-level, from left to right on each level

cur = root

Every iteration, the next pointers of a node's child will be updated

if(cur -> left) {
	cur -> left -> next = cur -> right;
	if(cur -> next) cur -> right -> next = cur -> next -> left;
}

	Move to next level

root = root -> left
// next iteration
cur = root

& repeat:

if(cur -> left) {
	cur -> left -> next = cur -> right;
	if(cur -> next) cur -> right -> next = cur -> next -> left;
}

	Continue the same process with all nodes on current level

for(; cur; cur = cur -> next)
    // ...

	No child node exists

if(cur -> left)
    // ...
else break

So, we break here. On the next iteration, root becomes NULL as well and we stop the process.

C++

class Solution {
public:
    Node* connect(Node* root) {
        auto head = root;
        for(; root; root = root -> left)
            for(auto cur = root; cur; cur = cur -> next)   // traverse each level - it's just BFS taking advantage of next pointers
                if(cur -> left) {                          // update next pointers of children if they exist
                    cur -> left -> next = cur -> right;
                    if(cur -> next) cur -> right -> next = cur -> next -> left;
                }
                else break;                                // if no children exist, stop iteration

        return head;
    }
};

Python

class Solution:
    def connect(self, root):
        head = root
        while root:
            cur, root = root, root.left
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                    if cur.next: cur.right.next = cur.next.left
                else: break
                cur = cur.next

        return head

Java

class Solution {
    public Node connect(Node root) {
        Node head = root;
        for(; root != null; root = root.left)
            for(Node cur = root; cur != null; cur = cur.next)
                if(cur.left != null) {
                    cur.left.next = cur.right;
                    if(cur.next != null) cur.right.next = cur.next.left;
                } else break;

        return head;
    }
}

Time Complexity : O(N), we only traverse each node once, basically doing a standard BFS.
Space Complexity : O(1), only constant extra space is being used


'''
