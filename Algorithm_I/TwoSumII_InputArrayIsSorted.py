# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
#
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
#
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
#
# Your solution must use only constant extra space.
#
#
#
# Example 1:
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
#
# Example 2:
#
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
#
# Example 3:
#
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

# The first solution I came up will iteratively go through each pair's sum
# which returned 'Time Limit Exceeded'
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]

# 218 ms, 14.9 MB
class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left <= right:
            summation = numbers[left] + numbers[right]
            if summation == target:
                return [left + 1, right + 1]
            elif summation < target:
                left += 1
            else:
                right -= 1


# user OldCodingFarmer's solutions
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/discuss/51249/Python-different-solutions-(two-pointer-dictionary-binary-search).

# dictionary
# 196 ms, 15.2 MB
def twoSum2(self, numbers, target):
    dic = {}
    for i, num in enumerate(numbers):
        if target-num in dic:
            return [dic[target-num]+1, i+1]
        dic[num] = i

# binary search, modified by user: ahoosh
# 254 ms, 15 MB
def twoSum3(self, numbers, target):
    investigatedSoFar = []
    for i in range(len(numbers)):
        if not numbers[i] in investigatedSoFar:
            investigatedSoFar.append(numbers[i])
            l, r = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l) // 2
                if numbers[mid] == tmp:
                    return([i + 1, mid + 1])
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1

# user zzzsoton's take on two pointers (fastest)
# 144 ms, 14.8 MB
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f, l = 0, len(numbers)-1;
        while numbers[f]+numbers[l] != target:
            if numbers[f]+numbers[l] > target:
                l -= 1;
            else:
                f +=1;
        return [f+1,l+1]
