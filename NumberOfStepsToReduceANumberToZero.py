# Given an integer num, return the number of steps to reduce it to zero.
#
# In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while num != 0:
            if num % 2 == 0:
                num /= 2
                counter += 1
            else:
                num -= 1
                counter += 1
        return counter

# this first solution that I came up with had runtime of 64 ms (very slow)
# to improve runtime, we can use the same technique used in FizzBuzz

# This solution had runtime of 43 ms
class Solution2:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while num != 0:
            divisible_by_2 = (num % 2 == 0)
            if divisible_by_2:
                num /= 2
                counter += 1
            else:
                num -= 1
                counter += 1
        return counter

### Discussion board C++ solution by _Aditya_Hedge_ that I find interesting
# // Iterative solution
# class Solution {
# public:
#     int numberOfSteps(int num) {
# 	// Overall count of steps
#         int count=0;
#
#         while(num!=0){
#             if(num%2==0){
#                 num/=2;
#                 count++;
#             }
#             else{
#                 num-=1;
#                 count++;
#             }
#         }
#         return count;
#     }
# 	// Recursive Solution
# 	if(num==0){
#           return 0;
#         }
#         return 1 + ((num%2==0)?numberOfSteps(num/2):numberOfSteps(num-1));
# };
