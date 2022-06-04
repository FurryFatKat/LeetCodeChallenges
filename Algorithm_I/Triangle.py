# Given a triangle array, return the minimum path sum from top to bottom.
#
# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
#
#
#
# Example 1:
#
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
#
# Example 2:
#
# Input: triangle = [[-10]]
# Output: -10


# https://leetcode.com/problems/triangle/discuss/38735/Python-easy-to-understand-solutions-(top-down-bottom-up).

# O(n*n/2) space, top-down
def minimumTotal1(self, triangle):
    if not triangle:
        return
    res = [[0 for i in xrange(len(row))] for row in triangle]
    res[0][0] = triangle[0][0]
    for i in xrange(1, len(triangle)):
        for j in xrange(len(triangle[i])):
            if j == 0:
                res[i][j] = res[i-1][j] + triangle[i][j]
            elif j == len(triangle[i])-1:
                res[i][j] = res[i-1][j-1] + triangle[i][j]
            else:
                res[i][j] = min(res[i-1][j-1], res[i-1][j]) + triangle[i][j]
    return min(res[-1])

# Modify the original triangle, top-down
def minimumTotal2(self, triangle):
    if not triangle:
        return
    for i in xrange(1, len(triangle)):
        for j in xrange(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
    return min(triangle[-1])

# Modify the original triangle, bottom-up
def minimumTotal3(self, triangle):
    if not triangle:
        return
    for i in xrange(len(triangle)-2, -1, -1):
        for j in xrange(len(triangle[i])):
            triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]

# bottom-up, O(n) space
def minimumTotal(self, triangle):
    if not triangle:
        return
    res = triangle[-1]
    for i in xrange(len(triangle)-2, -1, -1):
        for j in xrange(len(triangle[i])):
            res[j] = min(res[j], res[j+1]) + triangle[i][j]
    return res[0]


'''
https://leetcode.com/problems/triangle/discuss/38827/One-liner-in-Python

def minimumTotal(self, t):
    return reduce(lambda a,b:[f+min(d,e)for d,e,f in zip(a,a[1:],b)],t[::-1])[0]

Explanation

Starting with the bottom row, I move upwards, always combining the current row and the next upper row. At the end, I have combined everything into the top row and simply return its only element. Here's a longer version with meaningful variable names:

def minimumTotal(self, triangle):
    def combine_rows(lower_row, upper_row):
        return [upper + min(lower_left, lower_right)
                for upper, lower_left, lower_right in
                zip(upper_row, lower_row, lower_row[1:])]
    return reduce(combine_rows, triangle[::-1])[0]



'''

'''

https://leetcode.com/problems/triangle/discuss/38730/DP-Solution-for-Triangle

This problem is quite well-formed in my opinion. The triangle has a tree-like structure, which would lead people to think about traversal algorithms such as DFS. However, if you look closely, you would notice that the adjacent nodes always share a 'branch'. In other word, there are overlapping subproblems. Also, suppose x and y are 'children' of k. Once minimum paths from x and y to the bottom are known, the minimum path starting from k can be decided in O(1), that is optimal substructure. Therefore, dynamic programming would be the best solution to this problem in terms of time complexity.

What I like about this problem even more is that the difference between 'top-down' and 'bottom-up' DP can be 'literally' pictured in the input triangle. For 'top-down' DP, starting from the node on the very top, we recursively find the minimum path sum of each node. When a path sum is calculated, we store it in an array (memoization); the next time we need to calculate the path sum of the same node, just retrieve it from the array. However, you will need a cache that is at least the same size as the input triangle itself to store the pathsum, which takes O(N^2) space. With some clever thinking, it might be possible to release some of the memory that will never be used after a particular point, but the order of the nodes being processed is not straightforwardly seen in a recursive solution, so deciding which part of the cache to discard can be a hard job.

'Bottom-up' DP, on the other hand, is very straightforward: we start from the nodes on the bottom row; the min pathsums for these nodes are the values of the nodes themselves. From there, the min pathsum at the ith node on the kth row would be the lesser of the pathsums of its two children plus the value of itself, i.e.:

minpath[k][i] = min( minpath[k+1][i], minpath[k+1][i+1]) + triangle[k][i];

Or even better, since the row minpath[k+1] would be useless after minpath[k] is computed, we can simply set minpath as a 1D array, and iteratively update itself:

For the kth level:
minpath[i] = min( minpath[i], minpath[i+1]) + triangle[k][i];

Thus, we have the following solution

int minimumTotal(vector<vector<int> > &triangle) {
    int n = triangle.size();
    vector<int> minlen(triangle.back());
    for (int layer = n-2; layer >= 0; layer--) // For each layer
    {
        for (int i = 0; i <= layer; i++) // Check its every 'node'
        {
            // Find the lesser of its two children, and sum the current value in the triangle with it.
            minlen[i] = min(minlen[i], minlen[i+1]) + triangle[layer][i];
        }
    }
    return minlen[0];
}


'''




'''
# https://leetcode.com/problems/triangle/discuss/38737/Bottom-Up-5-line-C%2B%2B-Solution

class Solution {
public:
    int minimumTotal(vector<vector<int> > &triangle)
    {
        vector<int> mini = triangle[triangle.size()-1];
        for ( int i = triangle.size() - 2; i>= 0 ; --i )
            for ( int j = 0; j < triangle[i].size() ; ++ j )
                mini[j] = triangle[i][j] + min(mini[j],mini[j+1]);
        return mini[0];
    }
};

'''



'''

https://leetcode.com/problems/triangle/discuss/1169431/Short-and-Simple-Solutions-w-Explanation-or-4-Lines-of-Code-w-Comments

✔️ Solution - I (In-Place Bottom-Up Dynamic Programming)

We can easily see that directly just choosing the minimum value in the next row(amongst triangle[nextRow][i] and triangle[nextRow][i+1]) won't fetch us the optimal final result since it maybe the case that the latter values of previous chosen path turn out to be huge.

We need to observe that to get the minimum possible sum, we must use a path that has Optimal Value for each intermediate stop in the path. Thus, we can use Dynamic Programming to find the optimal value to reach each position of the triangle level by level. We can do this by accumulating the sum of path(or more specifically sum of values of optimal stops in a path) for each cell of a level from top to the bottom of triangle.

We are given that, at each cell in the triangle, we can move to the next row using two choices -

    Move to the same index i.
    Move to the next index i + 1

Since we are following a bottom-up approach, the above can also be interpreted as :-

For cell in the triangle, we could have reached here either from the previous row/level either from -

    the same index i, or
    the index i - 1

So, obviously the optimal choice to arrive at the current position in triangle would be to come from the cell having minimum value of these two choices.

We will keep adding the result from the lower level to the next/higher level by each time choosing the optimal cell to arrive at the current cell. Finally, we can return the minimum value that we get at the bottom-most row of the triangle. Here, no auxillary space is used and I have modified the triangle itself to achieve a space complexity of O(1).

C++

int minimumTotal(vector<vector<int>>& triangle) {
	// start from level 1 till the bottom-most level. Each time determine the best path to arrive at current cell
	for(int level = 1; level < size(triangle); level++)
		for(int i = 0; i <= level; i++)  // triangle[level].size() == level + 1 (level starts from 0)
			// for the current level:
			triangle[level][i] += min(triangle[level - 1][min(i, (int)size(triangle[level - 1]) - 1)], // we can either come from previous level and same index
			                          triangle[level - 1][max(i - 1, 0)]); // or the previous level and index-1
	// finally return the last element of the bottom level
	return *min_element(begin(triangle.back()), end(triangle.back()));
}

Python

def minimumTotal(self, triangle: List[List[int]]) -> int:
    for level in range(1, len(triangle)):
        for i in range(level+1):
            triangle[level][i] += min(triangle[level-1][min(i, level-1)], triangle[level-1][max(i-1,0)])
    return min(triangle[-1])

Time Complexity : O(N^2), where N are the total number of levels in triangle.
Space Complexity : O(1)

The min and max in the above code are used to do bound-checks.

✔️ Solution - II (In-Place Top-Down Dynamic Programming)

We chose to go from top-level to the bottom-level of triangle in the previous approach. We can also choose to start from the bottom of triangle and move all the way to the top. We will again follow the same DP strategy as used in the above solution.

At each cell of the triangle, we could have moved here from the below level in 2 ways, either from -

    the same index i in below row, or
    the index i+1.

And again, we will choose the minimum of these two to arrive at the optimal solution. Finally at last, we will reach at triangle[0][0], which will hold the optimal (minimum) sum of path.

Actually, this approach will make the code a lot more clean and concise by avoiding the need of bound checks.

C++

int minimumTotal(vector<vector<int>>& triangle) {
	for(int level = size(triangle) - 2; level >= 0; level--) // start from bottom-1 level
		for(int i = 0; i <= level; i++)
			 // for every cell: we could have moved here from same index or index+1 of next level
			triangle[level][i] += min(triangle[level + 1][i], triangle[level + 1][i + 1]);
	return triangle[0][0]; // lastly t[0][0] will contain accumulated sum of minimum path
}

Python

def minimumTotal(self, triangle: List[List[int]]) -> int:
    for level in range(len(triangle)-2,-1,-1):
        for i in range(level+1):
            triangle[level][i] += min(triangle[level+1][i], triangle[level+1][i+1])
    return triangle[0][0]

Time Complexity : O(N^2)
Space Complexity : O(1)

Solution - III (Bottom-Up Dynamic Programming w/ Auxillary Space)

More often than not, you would not be allowed to modify the given input. In such a situation, we can obviously opt for making a copy of the given input(triangle in this case). This would lead to a space complexity of O(N^2). I won't show this solution since the only change needed in above solutions would be adding the line vector<vector<int>>dp(triangle); and replacing triangle with dp (Or better yet just pass triangle by value instead of reference & keep using that itself 🤷‍♂️).

Here, I will present a solution with linear space complexity without input modification. We can observe in the above solutions that we really ever access only two rows of the input at the same time. So, we can just maintain two rows and alternate between those two in our loop.

I have used level & 1 in the below solution to alternate between these two rows of dp. It's very common way to go when we are converting from 2d DP to linear space. If you are not comfortable with it, you can also choose to maintain two separate rows and swap them at end of each iteration.

All the other things and idea remains the same as in the solution - I

C++

int minimumTotal(vector<vector<int>>& triangle) {
	int n = size(triangle), level = 1;
	vector<vector<int> > dp(2, vector<int>(n, INT_MAX));
	dp[0][0]=triangle[0][0];  // assign top-most row to dp[0] as we will be starting from level 1
	for(; level < n; level++)
		for(int i = 0; i <= level; i++)
			dp[level & 1][i] = triangle[level][i] + min(dp[(level - 1) & 1][min(i, n - 1)], dp[(level - 1) & 1][max(i - 1, 0)]);
	level--; // level becomes n after for loop ends. We need minimum value from level - 1
	return *min_element(begin(dp[level & 1]), end(dp[level & 1]));
}

Python

The below solution is using the two separate rows method that I described above and swapping after each iteration to alternate between them -

def minimumTotal(self, triangle: List[List[int]]) -> int:
	n = len(triangle)
	cur_row, prev_row = [0]*n, [0]*n
	prev_row[0] = triangle[0][0]
	for level in range(1, n):
		for i in range(level+1):
			cur_row[i] = triangle[level][i] + min(prev_row[min(i, level-1)], prev_row[max(i-1,0)])
		cur_row, prev_row = prev_row, cur_row
	return min(prev_row)

Time Complexity : O(N^2)
Space Complexity : O(N)

Solution - IV (Top-Down Dynamic Programming w/ Auxillary Space)

Here is the Top-Down version of Solution - II, without input array modification and using linear auxillary space.

C++

int minimumTotal(vector<vector<int>>& triangle) {
	int n = size(triangle), level = n - 1;
	vector<vector<int> > dp(2, vector<int>(n, 0));
	dp[level-- & 1] = triangle[n - 1];
	for(; level >= 0; level--)
		for(int i = 0; i <= level; i++)
			dp[level & 1][i] = triangle[level][i] + min(dp[(level + 1) & 1][i], dp[(level + 1) & 1][i + 1]);
	return dp[0][0];
}

Python

Again, I have used to two separate rows method here -

def minimumTotal(self, triangle: List[List[int]]) -> int:
    n = len(triangle)
    cur_row, next_row = [0]*n, triangle[n-1]
    for level in range(n-2,-1,-1):
        for i in range(level+1):
            cur_row[i] = triangle[level][i] + min(next_row[i], next_row[i+1])
        cur_row, next_row = next_row, cur_row
    return next_row[0]

Time Complexity : O(N^2)
Space Complexity : O(N)

'''
