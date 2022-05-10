# Write a function that reverses a string. The input string is given as an array of characters s.
#
# You must do this by modifying the input array in-place with O(1) extra memory.
#
#
#
# Example 1:
#
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
#
# Example 2:
#
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

# 219 ms, 18.7 MB
# if there are two strings, we are back-filling the second string
# to get the result, so that's how we will solve it
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s2= s.copy()
        left = 0
        right = len(s) - 1
        while left <= len(s) - 1:
            s[right] = s2[left]
            left += 1
            right -= 1

# One line solution by DBabichev
# https://leetcode.com/problems/reverse-string/discuss/669571/Python-Oneliner-two-pointers-explained
# 215 ms, 18.4 MB
class Solution:
    def reverseString(self, s):
        for i in range(len(s)//2): s[i], s[-i-1] = s[-i-1], s[i]



'''
C++ Solution by xz2210
https://leetcode.com/problems/reverse-string/discuss/80935/Simple-C%2B%2B-solution

class Solution {
public:
    string reverseString(string s) {
        int i = 0, j = s.size() - 1;
        while(i < j){
            swap(s[i++], s[j--]);
        }

        return s;
    }
};

'''
