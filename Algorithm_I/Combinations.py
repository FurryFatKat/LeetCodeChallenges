# Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
#
# You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#
# Example 2:
#
# Input: n = 1, k = 1
# Output: [[1]]




'''
Python


https://leetcode.com/problems/combinations/discuss/27024/1-liner-3-liner-4-liner


Library - AC in 64 ms

First the obvious solution - Python already provides this functionality and it's not forbidden, so let's take advantage of it.

from itertools import combinations

class Solution:
    def combine(self, n, k):
        return list(combinations(range(1, n+1), k))

Recursive - AC in 76 ms

But doing it yourself is more interesting, and not that hard. Here's a recursive version.

class Solution:
    def combine(self, n, k):
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]

Thanks to @boomcat for pointing out to use range(k, n+1) instead of my original range(1, n+1).

Iterative - AC in 76 ms

And here's an iterative one.

class Solution:
    def combine(self, n, k):
        combs = [[]]
        for _ in range(k):
            combs = [[i] + c for c in combs for i in range(1, c[0] if c else n+1)]
        return combs

Reduce - AC in 76 ms

Same as that iterative one, but using reduce instead of a loop:

class Solution:
  def combine(self, n, k):
    return reduce(lambda C, _: [[i]+c for c in C for i in range(1, c[0] if c else n+1)],
                  range(k), [[]])


'''




'''
C++

https://leetcode.com/problems/combinations/discuss/26992/Short-Iterative-C%2B%2B-Answer-8ms

class Solution {
public:
	vector<vector<int>> combine(int n, int k) {
		vector<vector<int>> result;
		int i = 0;
		vector<int> p(k, 0);
		while (i >= 0) {
			p[i]++;
			if (p[i] > n) --i;
			else if (i == k - 1) result.push_back(p);
			else {
			    ++i;
			    p[i] = p[i - 1];
			}
		}
		return result;
	}
};



'''
