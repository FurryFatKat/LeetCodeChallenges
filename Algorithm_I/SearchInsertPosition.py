# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
#
# Example 1:
#
# Input: nums = [1,3,5,6], target = 5
# Output: 2
#
# Example 2:
#
# Input: nums = [1,3,5,6], target = 2
# Output: 1
#
# Example 3:
#
# Input: nums = [1,3,5,6], target = 7
# Output: 4

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] == target:
                    return mid
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

# my first submission above has 90 ms runtime and 14.6MB Memory, but the first section
# feels like cheating

# my second submission yields 83 ms runtime, surprisingly faster.
# I am assuming that the number does not exist in the list, so we
# saved runtime by removing that initial check.
# This solution however, uses 0.2 MB more memory.
class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

# Looking through the discussion board and testing the solutions.
# It was found that defining the edge case will improve time and space complexity.
# 77 ms runtime and 14.7MB memory
class Solution3:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        if target == nums[len(nums)-1]:
            return len(nums)-1
        if target > nums[len(nums)-1]:
            return len(nums)
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left
