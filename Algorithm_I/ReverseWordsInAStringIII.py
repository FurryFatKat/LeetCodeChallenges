# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
#
#
# Example 1:
#
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
#
# Example 2:
#
# Input: s = "God Ding"
# Output: "doG gniD"

# 52 ms, 14.8 MB
# my first take does not comply with the two pointer methodology
class Solution:
    def reverseWords(self, s: str) -> str:
        output = ''
        s_list = s.split()
        for word in s_list:
            output += word[::-1] + ' '

        return output[:-1]
