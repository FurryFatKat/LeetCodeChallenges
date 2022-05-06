# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
#
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
#
# Example 2:
#
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        else:
            return nums.index(target)

# the above solution (my first solution) has runtime of 262 ms, but it isn't exactly
# a binary search function

# I re-wrote a binary search function:
# looping through the list and if a match is not found, we return -1
# a counter is used to return index of the current match
# After submission, runtime is 465 ms
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        counter = 0
        while nums[0] <= target <= nums[-1]:
            half_length = len(nums)//2
            if target == nums[half_length]:
                counter += half_length
                return counter
            elif target > nums[half_length]:
                counter += half_length + 1
                nums = nums[half_length+1:]
            else:
                nums = nums[:half_length]

        return -1


# Some references: https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html

# LeetCode Solution:
# Algorithm
#
#     Initialise left and right pointers : left = 0, right = n - 1.
#
#     While left <= right :
#
#         Compare middle element of the array nums[pivot] to the target value target.
#
#             If the middle element is the target target = nums[pivot] : return pivot.
#
#             If the target is not yet found :
#
#                 If target < nums[pivot], continue the search on the left right = pivot - 1.
#
#                 Else continue the search on the right left = pivot + 1.

# LeetCode solution has runtime of 252 ms!
# this is much faster than my second solution, most likely due to
# not having to re-assign nums, and instead just move the pointers
class LeetCodeSolution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1



'''
// LeetCode C++ Solution

class Solution {
  public:
  int search(vector<int>& nums, int target) {
    int pivot, left = 0, right = nums.size() - 1;
    while (left <= right) {
      pivot = left + (right - left) / 2;
      if (nums[pivot] == target) return pivot;
      if (target < nums[pivot]) right = pivot - 1;
      else left = pivot + 1;
    }
    return -1;
  }
};
'''
