# Given an integer n, return a string array answer (1-indexed) where:
#
#     answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#     answer[i] == "Fizz" if i is divisible by 3.
#     answer[i] == "Buzz" if i is divisible by 5.
#     answer[i] == i (as a string) if none of the above conditions are true.

# Question to be answered before starting:
# how to check if a number is divisible by another?
# >>> 1/3
# 0.3333333333333333
# >>> 1//3
# 0
# >>> 2//3
# 0
# >>> 3//3
# 1
# >>> 15//3
# 5
# >>> 15//5
# 3
# >>> 4//3
# 1
# >>> 4%3
# 1
# >>> 3%3
# 0
# >>> 15%3
# 0
# >>> 15%5
# 0
# based on the quick test above, modulus is what we will use


# this solution runtime was 92 ms (very slow)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        i = 1
        fb_list = []
        while i <= n:
            if i%5 == 0 and i%3 == 0:
                fb_list.append("FizzBuzz")
            elif i%3 == 0:
                fb_list.append("Fizz")
            elif i%5 == 0:
                fb_list.append("Buzz")
            else:
                fb_list.append(str(i))
            i += 1
        return fb_list

# checking the solution in LeetCode
# Approach 3 to store fizzbuzz mappings in dictionary
# improving time and space complexity
class LeetCodeSolution:
    def fizzBuzz(self, n: int) -> List[str]:
        i = 1
        fb_list = []
        fb_dict = {
            3 : "Fizz",
            5 : "Buzz"}
        while i <= n:
            ans_str = ""
            for key in fb_dict.keys():
                if i % key == 0:
                    ans_str += fb_dict[key]

            if not ans_str:
                ans_str = str(i)
            i += 1
            fb_list.append(ans_str)
        return fb_list
