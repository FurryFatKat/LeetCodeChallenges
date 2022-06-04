# You are a professional robber planning to rob houses along
# a street. Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them
# is that adjacent houses have security systems connected and
# it will automatically contact the police if two adjacent houses
# were broken into on the same night.
#
# Given an integer array nums representing the amount of money
# of each house, return the maximum amount of money you can rob
# tonight without alerting the police.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
#
# Example 2:
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

# my first solution only goes through two of the possible permutation
class Solution:
    def rob(self, nums: List[int]) -> int:
        non_d = 0
        d = 0
        for i in range(len(nums)):
            if i%2 == 0:
                d += nums[i]
            else:
                non_d += nums[i]
            print('d: ', d, ' non_d: ', non_d)

        return max(d, non_d)


'''
https://leetcode.com/problems/house-robber/discuss/55696/Python-solution-3-lines.

Based on the recursive formula:

    f(0) = nums[0]
    f(1) = max(num[0], num[1])
    f(k) = max( f(k-2) + nums[k], f(k-1) )
'''

class Solution:

    def rob(self, nums):

        last, now = 0, 0

        for i in nums: last, now = now, max(last + i, now)

        return now

'''
For anyone who still needs help understanding the coding logic,
it's actually pretty straightforward than it looks. The only key
idea we have to understand is that we want to store previous
values (very much similar to if we were swapping two variables).
Here is a much more simplified version of the logic with comments.
Let me know if it helps!

'''
class Solution(object):
  def rob(self, nums):
    # Base Case: nums[0] = nums[0]
    # nums[1] = max(nums[0], nums[1])
    # nums[k] = max(k + nums[k-2], nums[k-1])
    '''
    # Approach 1:- Construct dp table
    if not nums: return 0
    if len(nums) == 1: return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
      dp[i] = max(nums[i] + dp[i-2], dp[i-1])
    return dp[-1] # return the last element
    '''

    # Approach 2:- Constant space use two variables and compute the max respectively
    prev = curr = 0
    for num in nums:
      temp = prev # This represents the nums[i-2]th value
      prev = curr # This represents the nums[i-1]th value
      curr = max(num + temp, prev) # Here we just plug into the formula
    return curr






'''
https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.

There is some frustration when people publish their perfect fine-grained algorithms without sharing any information abut how they were derived. This is an attempt to change the situation. There is not much more explanation but it's rather an example of higher level improvements. Converting a solution to the next step shouldn't be as hard as attempting to come up with perfect algorithm at first attempt.

This particular problem and most of others can be approached using the following sequence:

    Find recursive relation
    Recursive (top-down)
    Recursive + memo (top-down)
    Iterative + memo (bottom-up)
    Iterative + N variables (bottom-up)

Step 1. Figure out recursive relation.
A robber has 2 options: a) rob current house i; b) don't rob current house.
If an option "a" is selected it means she can't rob previous i-1 house but can safely proceed to the one before previous i-2 and gets all cumulative loot that follows.
If an option "b" is selected the robber gets all the possible loot from robbery of i-1 and all the following buildings.
So it boils down to calculating what is more profitable:

    robbery of current house + loot from houses before the previous
    loot from the previous house robbery and any loot captured before that

rob(i) = Math.max( rob(i - 2) + currentHouseValue, rob(i - 1) )

Step 2. Recursive (top-down)
Converting the recurrent relation from Step 1 shound't be very hard.

public int rob(int[] nums) {
    return rob(nums, nums.length - 1);
}
private int rob(int[] nums, int i) {
    if (i < 0) {
        return 0;
    }
    return Math.max(rob(nums, i - 2) + nums[i], rob(nums, i - 1));
}

This algorithm will process the same i multiple times and it needs improvement. Time complexity: [to fill]

Step 3. Recursive + memo (top-down).

int[] memo;
public int rob(int[] nums) {
    memo = new int[nums.length + 1];
    Arrays.fill(memo, -1);
    return rob(nums, nums.length - 1);
}

private int rob(int[] nums, int i) {
    if (i < 0) {
        return 0;
    }
    if (memo[i] >= 0) {
        return memo[i];
    }
    int result = Math.max(rob(nums, i - 2) + nums[i], rob(nums, i - 1));
    memo[i] = result;
    return result;
}

Much better, this should run in O(n) time. Space complexity is O(n) as well, because of the recursion stack, let's try to get rid of it.

Step 4. Iterative + memo (bottom-up)

public int rob(int[] nums) {
    if (nums.length == 0) return 0;
    int[] memo = new int[nums.length + 1];
    memo[0] = 0;
    memo[1] = nums[0];
    for (int i = 1; i < nums.length; i++) {
        int val = nums[i];
        memo[i+1] = Math.max(memo[i], memo[i-1] + val);
    }
    return memo[nums.length];
}

Step 5. Iterative + 2 variables (bottom-up)
We can notice that in the previous step we use only memo[i] and memo[i-1], so going just 2 steps back. We can hold them in 2 variables instead. This optimization is met in Fibonacci sequence creation and some other problems [to paste links].

/* the order is: prev2, prev1, num  */
public int rob(int[] nums) {
    if (nums.length == 0) return 0;
    int prev1 = 0;
    int prev2 = 0;
    for (int num : nums) {
        int tmp = prev1;
        prev1 = Math.max(prev2 + num, prev1);
        prev2 = tmp;
    }
    return prev1;
}


'''




'''

https://leetcode.com/problems/house-robber/discuss/55693/C-1ms-O(1)space-very-simple-solution

#define max(a, b) ((a)>(b)?(a):(b))
int rob(int num[], int n) {
    int a = 0;
    int b = 0;

    for (int i=0; i<n; i++)
    {
        if (i%2==0)
        {
            a = max(a+num[i], b);
        }
        else
        {
            b = max(a, b+num[i]);
        }
    }

    return max(a, b);
}

'''




'''

https://leetcode.com/problems/house-robber/discuss/1605797/C%2B%2BPython-4-Simple-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP


We are given an array of money in each house A and we need to return the maximum amount we can rob without robbing from any two adjacent houses.

❌ Solution - I (Brute-Force)

Let's try solving with brute-force approach. For each house, we have two choices -

    Dont rob the house and move to next house.
    Rob the house and move to the house after next house (We dont move directly to next house because we can rob adjacent houses).

So, we will just try with both these choices and choose the one the yields the maximum amount of loot.

C++

class Solution {
public:
    int rob(vector<int>& A, int i = 0) {
        return i < size(A) ? max(rob(A, i+1), A[i] + rob(A, i+2)) : 0;
    }
};

Python

class Solution:
    def rob(self, A, i = 0):
        return max(self.rob(A, i+1), A[i] + self.rob(A, i+2)) if i < len(A) else 0

Time Complexity : O(2N), where N is the number of elements in A. At each index, we have two choices of either robbing or not robbing the current house. Thus this leads to time complexity of 2*2*2...n times ≈ O(2N)
Space Complexity : O(N), required by implicit recursive stack. The max depth of recursion can go upto N.

✔️ Solution - II (Dynamic Programming - Memoization)

In the above solution, we were performing many redundant repeated computations. This can be observed by drawing out the recursive tree for above function and observing that rob(i) is called multiple times. But rob(i) is nothing but the maximum amount of loot we can get starting at index i and this amount remains the same at each call.

So, instead of re-computing multiple times, we can store the result of a function call and directly reuse it on future calls instead of recomputing from scratch. This calls for dynamic programming, or memoization to be more specific. Here, we can use a linear dp array where dp[i] will denote the maximum amount of loot we can get starting at i index. Initially all elements of dp are initialized to -1 denoting they haven't been computed yet, Each time, we will save the computed result in this dp for an index i and directly return it if a future call is made to this index.

C++

class Solution {
public:
    int rob(vector<int>& A) {
        vector<int> dp(size(A),-1);
        return rob(A, dp, 0);
    }
    int rob(vector<int>& A, vector<int>& dp, int i) {
        if(i >= size(A)) return 0;
        if(dp[i] != -1) return dp[i];
        return dp[i] = max(rob(A, dp, i+1), A[i] + rob(A, dp, i+2));
    }
};

    One-Liner

Python

class Solution:
    def rob(self, A):
        @cache
        def rob(i):
            return max(rob(i+1), A[i] + rob(i+2)) if i < len(A) else 0
        return rob(0)

Time Complexity : O(N), We calculate the result for each index only once & there are N indices. Thus overall time complexity is O(N).
Space Complexity : O(N), required for dp and implicit recursive stack.

✔️ Solution - III (Dynamic Programming - Tabulation)

We can implement the same logic as above in an iterate approach as well. Here, we again use a dp array to save the results of computation. In this case, dp[i] will denote maximum loot that we can get by considering till ith index. At every index,

    We can keep same loot as we had at previous index - dp[i-1]
    Or, we can rob the current house and add it to the loot we have at i-2th index - A[i] + dp[i-2]

C++

class Solution {
public:
    int rob(vector<int>& A) {
        if(size(A) == 1) return A[0];
        vector<int> dp(A);
        dp[1] = max(A[0], A[1]);
        for(int i = 2; i < size(A); i++)
            dp[i] = max(dp[i-1], A[i] + dp[i-2]);
        return dp.back();
    }
};

Python

class Solution:
    def rob(self, A):
        if len(A) == 1: return A[0]
        dp = [*A]
        dp[1] = max(A[0], A[1])
        for i in range(2, len(A)):
            dp[i] = max(dp[i-1], A[i] + dp[i-2])
        return dp[-1]

Time Complexity : O(N), just single iteration is performed from 2 to N to compute each dp[i].
Space Complexity : O(N), required for dp.

✔️ Solution - IV (Space-Optimzed Dynamic Programming)

We can observe that the above dp solution relied only on the previous two indices in dp to compute the value of current dp[i]. So, we dont really need to maintain the whole dp array and can instead just maintain the values of previous index (denoted as prev below) and previous-to-previous index (denoted as prev2) and we can calculate the value for current index (cur) using just these two variables and roll-forward each time.

C++

class Solution {
public:
    int rob(vector<int>& A) {
        int prev2 = 0, prev = 0, cur = 0;
        for(auto i : A) {
            cur = max(prev, i + prev2);
            prev2 = prev;
            prev = cur;
        }
        return cur;
    }
};

Python

class Solution:
    def rob(self, A):
        prev2, prev, cur = 0,0,0
        for i in A:
            cur = max(prev, i + prev2)
            prev2 = prev
            prev = cur
        return cur

Time Complexity : O(N)
Space Complexity : O(1), only constant extra space is used.

'''
