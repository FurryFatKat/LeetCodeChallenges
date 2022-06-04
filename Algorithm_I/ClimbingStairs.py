# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
#
#
# Example 1:
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
# Example 2:
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# I tried to use DFS recursive to solve the problem, but
# the solution isn't viable

# https://leetcode.com/problems/climbing-stairs/discuss/1531764/Python-%3ADetail-explanation-(3-solutions-easy-to-difficult)-%3A-Recursion-dictionary-and-DP

'''

General inutution
-> Intution : the next distinict way of climbing stairs is euqal to the sum of the last two distinict way of climbing
distinct(n) = distinict(n-1) + distinict(n-2)
This intution can be applied using the following three approach --> ordered from easy to difficult approach
Idea 1 : pure recursive (Can't pass the test case :does not work for big number, result time-exced limit)
- The base case will be when only 1 or 2 steps left
- Result time-exced limit
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
         def climb(n):
             if n==1: #only one step option is availble
                 return 1
             if n ==2: # two options are possible : to take two 1-stpes or to only take one 2-steps
                 return 2
             return climb(n-1) + climb(n-2)
         return climb(n)


'''
Idea 2 : use dictionary (look-up table) to memorize repeating recursion
- The memory start with the base case and recored every recurssion
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo ={}
        memo[1] = 1
        memo[2] = 2

        def climb(n):
            if n in memo: # if the recurssion already done before first take a look-up in the look-up table
                return memo[n]
            else:   # Store the recurssion function in the look-up table and reuturn the stored look-up table function
                memo[n] =  climb(n-1) + climb(n-2)
                return memo[n]

        return climb(n)

'''
Idea 3 : Dynamic programming
--> store the distinct ways in a dynamic table
climb = [climb(0), climb(1), climb(2)=climb(0)+climb(1), climb(3)=climb(2)+climb(1),......climb(n)=climb(n-1)+climb(n-2)]
dp = [ 0, 1, 2, 3, 5, dp(i-1)+dp(i-2])]
return dp[n]
'''

def climb(n):
    #edge cases
    if n==0: return 0
    if n==1: return 1
    if n==2: return 2
    dp = [0]*(n+1) # considering zero steps we need n+1 places
    dp[1]= 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-1] +dp[i-2]
    print(dp)
    return dp[n]


'''
https://leetcode.com/problems/climbing-stairs/discuss/25296/3-4-short-lines-in-every-language


Same simple algorithm written in every offered language. Variable a tells you the number of ways to reach the current step, and b tells you the number of ways to reach the next step. So for the situation one step further up, the old b becomes the new a, and the new b is the old a+b, since that new step can be reached by climbing 1 step from what b represented or 2 steps from what a represented.

Ruby wins, and "the C languages" all look the same.

Ruby (60 ms)

def climb_stairs(n)
    a = b = 1
    n.times { a, b = b, a+b }
    a
end

C++ (0 ms)

int climbStairs(int n) {
    int a = 1, b = 1;
    while (n--)
        a = (b += a) - a;
    return a;
}

Java (208 ms)

public int climbStairs(int n) {
    int a = 1, b = 1;
    while (n-- > 0)
        a = (b += a) - a;
    return a;
}

Python (52 ms)

def climbStairs(self, n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a

C (0 ms)

int climbStairs(int n) {
    int a = 1, b = 1;
    while (n--)
        a = (b += a) - a;
    return a;
}

C# (48 ms)

public int ClimbStairs(int n) {
    int a = 1, b = 1;
    while (n-- > 0)
        a = (b += a) - a;
    return a;
}

Javascript (116 ms)

var climbStairs = function(n) {
    a = b = 1
    while (n--)
        a = (b += a) - a
    return a
};


'''


'''
https://leetcode.com/problems/climbing-stairs/discuss/25299/Basically-it's-a-fibonacci.

The problem seems to be a dynamic programming one. Hint: the tag also suggests that!
Here are the steps to get the solution incrementally.

    Base cases:
    if n <= 0, then the number of ways should be zero.
    if n == 1, then there is only way to climb the stair.
    if n == 2, then there are two ways to climb the stairs. One solution is one step by another; the other one is two steps at one time.

    The key intuition to solve the problem is that given a number of stairs n, if we know the number ways to get to the points [n-1] and [n-2] respectively, denoted as n1 and n2 , then the total ways to get to the point [n] is n1 + n2. Because from the [n-1] point, we can take one single step to reach [n]. And from the [n-2] point, we could take two steps to get there.

    The solutions calculated by the above approach are complete and non-redundant. The two solution sets (n1 and n2) cover all the possible cases on how the final step is taken. And there would be NO overlapping among the final solutions constructed from these two solution sets, because they differ in the final step.

Now given the above intuition, one can construct an array where each node stores the solution for each number n. Or if we look at it closer, it is clear that this is basically a fibonacci number, with the starting numbers as 1 and 2, instead of 1 and 1.

The implementation in Java as follows:

public int climbStairs(int n) {
    // base cases
    if(n <= 0) return 0;
    if(n == 1) return 1;
    if(n == 2) return 2;

    int one_step_before = 2;
    int two_steps_before = 1;
    int all_ways = 0;

    for(int i=2; i<n; i++){
    	all_ways = one_step_before + two_steps_before;
    	two_steps_before = one_step_before;
        one_step_before = all_ways;
    }
    return all_ways;
}




'''
