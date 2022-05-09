# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
#
#
#
# Example 1:
#
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Example 2:
#
# Input: nums = [0]
# Output: [0]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # using [0,1,0,3,12] as example input
        # let's write down the output by steppig through the elements in input
        # [, , , ,0]
        # [1, , , ,0]
        # [1, , ,0,0]
        # [1,3, , 0,0]
        # [1,3,12,0,0]

        # this tells us that we need two pointers to fill in the output list
        # and another to loop through the original list

        # 218 ms, 15.5MB
        nums2 = nums.copy()
        left = 0
        right = len(nums) - 1
        for i in range(len(nums)):
            if nums2[i] == 0:
                nums[right] = 0
                right -= 1
            else:
                nums[left] = nums2[i]
                left += 1
