# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
# Example 2:
#
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
#
# Example 3:
#
# Input: nums = [1]
# Output: [[1]]



'''
Python

https://leetcode.com/problems/permutations/discuss/18284/Backtrack-Summary%3A-General-Solution-for-10-Questions!!!!!!!!-Python-(Combination-Sum-Subsets-Permutation-Palindrome)

39. Combination Sum
https://leetcode.com/problems/combination-sum/

    def combinationSum(self, candidates, target):
        def backtrack(tmp, start, end, target):
            if target == 0:
                ans.append(tmp[:])
            elif target > 0:
                for i in range(start, end):
                    tmp.append(candidates[i])
                    backtrack(tmp, i, end, target - candidates[i])
                    tmp.pop()
        ans = []
        candidates.sort(reverse= True)
        backtrack([], 0, len(candidates), target)
        return ans

40. Combination Sum II
https://leetcode.com/problems/combination-sum-ii/

    def combinationSum2(self, candidates, target):
        def backtrack(start, end, tmp, target):
            if target == 0:
                ans.append(tmp[:])
            elif target > 0:
                for i in range(start, end):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    tmp.append(candidates[i])
                    backtrack(i+1, end, tmp, target - candidates[i])
                    tmp.pop()
        ans = []
        candidates.sort(reverse= True)
        backtrack(0, len(candidates), [], target)
        return ans

78. Subsets
https://leetcode.com/problems/subsets/

    def subsets(self, nums):
        def backtrack(start, end, tmp):
            ans.append(tmp[:])
            for i in range(start, end):
                tmp.append(nums[i])
                backtrack(i+1, end, tmp)
                tmp.pop()
        ans = []
        backtrack(0, len(nums), [])
        return ans

90. Subsets II
https://leetcode.com/problems/subsets-ii/

    def subsetsWithDup(self, nums):
        def backtrack(start, end, tmp):
            ans.append(tmp[:])
            for i in range(start, end):
                if i > start and nums[i] == nums[i-1]:
                    continue
                tmp.append(nums[i])
                backtrack(i+1, end, tmp)
                tmp.pop()
        ans = []
        nums.sort()
        backtrack(0, len(nums), [])
        return ans

46. Permutations
https://leetcode.com/problems/permutations/

    def permute(self, nums):
        def backtrack(start, end):
            if start == end:
                ans.append(nums[:])
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1, end)
                nums[start], nums[i] = nums[i], nums[start]

        ans = []
        backtrack(0, len(nums))
        return ans

47. Permutations II
https://leetcode.com/problems/permutations-ii/

    def permuteUnique(self, nums):
        def backtrack(tmp, size):
            if len(tmp) == size:
                ans.append(tmp[:])
            else:
                for i in range(size):
                    if visited[i] or (i > 0 and nums[i-1] == nums[i] and not visited[i-1]):
                        continue
                    visited[i] = True
                    tmp.append(nums[i])
                    backtrack(tmp, size)
                    tmp.pop()
                    visited[i] = False
        ans = []
        visited = [False] * len(nums)
        nums.sort()
        backtrack([], len(nums))
        return ans

60. Permutation Sequence
https://leetcode.com/problems/permutation-sequence/

    def getPermutation(self, n, k):
        nums = [str(i) for i in range(1, n+1)]
        fact = [1] * n
        for i in range(1,n):
            fact[i] = i*fact[i-1]
        k -= 1
        ans = []
        for i in range(n, 0, -1):
            id = k / fact[i-1]
            k %= fact[i-1]
            ans.append(nums[id])
            nums.pop(id)
        return ''.join(ans)

131. Palindrome Partitioning
https://leetcode.com/problems/palindrome-partitioning/

    def partition(self, s):
        def backtrack(start, end, tmp):
            if start == end:
                ans.append(tmp[:])
            for i in range(start, end):
                cur = s[start:i+1]
                if cur == cur[::-1]:
                    tmp.append(cur)
                    backtrack(i+1, end, tmp)
                    tmp.pop()
        ans = []
        backtrack(0, len(s), [])
        return ans

267. Palindrome Permutation II
https://leetcode.com/problems/palindrome-permutation-ii/
Related to this two:
31. Next Permutation: https://leetcode.com/problems/next-permutation/
266. Palindrome Permutation: https://leetcode.com/problems/palindrome-permutation/

    def generatePalindromes(self, s):
        kv = collections.Counter(s)
        mid = [k for k, v in kv.iteritems() if v%2]
        if len(mid) > 1:
            return []
        mid = '' if mid == [] else mid[0]
        half = ''.join([k * (v/2) for k, v in kv.iteritems()])
        half = [c for c in half]

        def backtrack(end, tmp):
            if len(tmp) == end:
                cur = ''.join(tmp)
                ans.append(cur + mid + cur[::-1])
            else:
                for i in range(end):
                    if visited[i] or (i>0 and half[i] == half[i-1] and not visited[i-1]):
                        continue
                    visited[i] = True
                    tmp.append(half[i])
                    backtrack(end, tmp)
                    visited[i] = False
                    tmp.pop()

        ans = []
        visited = [False] * len(half)
        backtrack(len(half), [])
        return ans



'''




'''
Java




'''




'''
C++



'''
