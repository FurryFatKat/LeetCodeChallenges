# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.
#
#
#
# Example 1:
#
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
#
# Example 2:
#
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

# https://leetcode.com/problems/permutation-in-string/discuss/1761953/Python3-SLIDING-WINDOW-OPTIMIZED-(-)-Explained
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        cntr, w, match = Counter(s1), len(s1), 0
        print(type(cntr))
        for i in range(len(s2)):
            if s2[i] in cntr:
                if not cntr[s2[i]]:
                    match -= 1
                cntr[s2[i]] -= 1
                if not cntr[s2[i]]:
                    match += 1

            if i >= w and s2[i-w] in cntr:
                if not cntr[s2[i-w]]:
                    match -= 1
                cntr[s2[i-w]] += 1
                if not cntr[s2[i-w]]:
                    match += 1

            if match == len(cntr):
                return True
        return False
