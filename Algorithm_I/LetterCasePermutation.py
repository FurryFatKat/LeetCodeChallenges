# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
#
# Return a list of all possible strings we could create. Return the output in any order.
#
#
#
# Example 1:
#
# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
#
# Example 2:
#
# Input: s = "3z4"
# Output: ["3z4","3Z4"]

'''
Python

https://leetcode.com/problems/letter-case-permutation/discuss/379928/Python-clear-solution

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def backtrack(sub="", i=0):
            if len(sub) == len(S):
                res.append(sub)
            else:
                if S[i].isalpha():
                    backtrack(sub + S[i].swapcase(), i + 1)
                backtrack(sub + S[i], i + 1)

        res = []
        backtrack()
        return res






'''
