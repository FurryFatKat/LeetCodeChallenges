# You are given two binary trees root1 and root2.
#
# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.
#
# Return the merged tree.
#
# Note: The merging process must start from the root nodes of both trees.
#
#
#
# Example 1:
#
# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]
#
# Example 2:
#
# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node1, node2):
            if node1 == None and node2 == None:
                return
            elif node1 == None:
                return
            elif node2 == None:
                # this only re-assigns node2 but not update root2
                node2 = node1
                return
            else:
                node2.val += node1.val
            [dfs(x, y) for (x,y) in ((node1.left, node2.left),(node1.right, node2.right)) ]
        dfs(root1, root2)
        return root2


# after some trying, I can't find a way to make the above method work
# instead, we will need to reconstruct a TreeNode for this

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            root = TreeNode(root1.val + root2.val)
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
            return root
        elif root1:
            return root1
        else:
            return root2

# https://leetcode.com/problems/merge-two-binary-trees/discuss/104301/Short-Recursive-Solution-w-Python-and-C%2B%2B
'''

python solution

class Solution(object):
    def mergeTrees(self, t1, t2):
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        else:
            return t1 or t2

c++ solution

class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if ( t1 && t2 ) {
            TreeNode * root = new TreeNode(t1->val + t2->val);
            root->left = mergeTrees(t1->left, t2->left);
            root->right = mergeTrees(t1->right, t2->right);
            return root;
        } else {
            return t1 ? t1 : t2;
        }
    }
};


'''

# https://leetcode.com/problems/merge-two-binary-trees/discuss/588123/~100.00-fast-in-run-time-and-memory-RecursiveIterativeBFSDFS

'''
Using Recursion (DFS Similar) 1:
Time complexity : O(m). A total of m nodes need to be traversed. Here, m represents the minimum number of nodes from the two given trees.
Space complexity : O(m). The depth of the recursion tree can go upto m in the case of a skewed tree. In average case, depth will be ****O(logm).

static int x = []() {
std::ios::sync_with_stdio(false);
cin.tie(nullptr);
return 0; }();

class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if(!t1) return t2;
        if(!t2) return t1;
        t1->val+=t2->val;
        if(t2->left) t1->left = mergeTrees(t1->left,t2->left);
        if(t2->right) t1->right = mergeTrees(t1->right,t2->right);
        return t1;
    }
};

Using Recursion (DFS Similar) 2:

class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if(!t1 && !t2) return nullptr;
        if(!t1) return t2;
        if(!t2) return t1;
        t1->val+=t2->val;
        t1->left = mergeTrees(t1->left,t2->left);
        t1->right = mergeTrees(t1->right,t2->right);
        return t1;
    }
};

Create New Tree 1:

class Solution {
public:
    void dfs(TreeNode* t1, TreeNode* t2,TreeNode* &root){
        if(!t1 && !t2) return;
        else if(t1 && !t2){
            TreeNode* node(new TreeNode(t1->val));
            root=node;
            dfs(t1->left,t2,root->left);
            dfs(t1->right,t2,root->right);
        }else if(t2 && !t1){
            TreeNode* node(new TreeNode(t2->val));
            root=node;
            dfs(t1,t2->left,root->left);
            dfs(t1,t2->right,root->right);
        }else{
            TreeNode* node(new TreeNode(t1->val+t2->val));
            root=node;
            dfs(t1->left,t2->left,root->left);
            dfs(t1->right,t2->right,root->right);
        }
    }
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        TreeNode* root(nullptr);
        dfs(t1,t2,root);
        return root;
    }
};

Create New Tree 2:
In the real world, sharing nodes between the old trees and the new tree can be a problem. If any of the old trees is deleted, it's going to also destruct the shared nodes in the new tree. C++ does have some nice & clean solutions for this, like using shared_ptr for example. But as-is I'd say the 'trick' of reusing nodes from the old trees does more harm than good and if I were the interviewer, unless the interviewee points these nuances out I'd be lead to believe that they don't have a good grasp on memory management in C++. Especially since the 'safe' solution is not that much more code:

class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if(!t1 && !t2) return nullptr;
        int val1 = t1? t1->val:0;
        int val2 = t2? t2->val:0;

        TreeNode* t = new TreeNode(val1+val2);
        t->left = mergeTrees(t1?t1->left:nullptr,t2?t2->left:nullptr);
        t->right = mergeTrees(t1?t1->right:nullptr,t2?t2->right:nullptr);
        return t;
    }
};

Iterative: Using Stack
Time complexity : O(n). We traverse over a total of n nodes. Here, nn refers to the smaller of the number of nodes in the two trees.

Space complexity : O(n). The depth of stack can grow upto n in case of a skewed tree.

class Solution { // iterative: Stack
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if(!t1 && !t2) return nullptr;
        if(!t1 || !t2) return t1? t1:t2;

        stack<TreeNode*> s1,s2;
        s1.push(t1);
        s2.push(t2);

        while(!s1.empty()){
            TreeNode* c1(s1.top());
            TreeNode* c2(s2.top());
            s1.pop();
            s2.pop();

            c1->val+=c2->val;

            if(!c1->left && c2->left) c1->left = c2->left;
            else if(c1->left && c2->left) { s1.push(c1->left); s2.push(c2->left); }

            if(!c1->right && c2->right) c1->right = c2->right;
            else if(c1->right && c2->right) { s1.push(c1->right); s2.push(c2->right); }
        }
        return t1;
    }
};

Iterative: Using Queue

class Solution { // iterative: Queue
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if(!t1 && !t2) return nullptr;
        if(!t1 || !t2) return t1? t1:t2;

        queue<TreeNode*> q1,q2;
        q1.push(t1);
        q2.push(t2);

        while(!q1.empty() && !q2.empty()){
            TreeNode* c1(q1.front());
            TreeNode* c2(q2.front());
            q1.pop();
            q2.pop();

            c1->val+=c2->val;

            if(!c1->left && c2->left) c1->left = c2->left;
            else if(c1->left && c2->left) { q1.push(c1->left); q2.push(c2->left); }

            if(!c1->right && c2->right) c1->right = c2->right;
            else if(c1->right && c2->right) { q1.push(c1->right); q2.push(c2->right); }
        }
        return t1;
    }
};


'''
