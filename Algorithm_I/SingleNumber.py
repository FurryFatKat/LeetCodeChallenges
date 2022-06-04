# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.
#
#
#
# Example 1:
#
# Input: nums = [2,2,1]
# Output: 1
#
# Example 2:
#
# Input: nums = [4,1,2,1,2]
# Output: 4
#
# Example 3:
#
# Input: nums = [1]
# Output: 1

# the magic of XOR!
# at first my brain fail to compute why we would need to
# perform bitwise operation for this question while
# we can use hashmap (dictionary) to solve for this


# https://leetcode.com/problems/single-number/discuss/1771771/Think-it-through-oror-Time%3A-O(n)-Space%3A-O(1)-oror-Python-Explained
'''
Edge Cases:

    No element appears twice; it is a constraint so not possible
    Single length array; return the only element already present in the array
    len(nums) > 1; find the single element that does not appear twice

Approaches:

    Brute Force
    Intuition:
    Iterate through every element in the nums and check if any of the element does not appear twice, in that case return the element.
    Time: O(n^2)
    Space: O(1)

    Use Sorting
    Intuition:
    If the elements of the nums array are sorted/when we sort it, we can compare the neighbours to find the single element. It is already mentioned that all other elements appear twice except one.
    Time: O(nlogn) for sorting then O(n) to check neighbouring elements
    Space: O(1)

    Use Hashing/Set
    Intuition:
    i) As we iterate through the nums array we store the elements encountered and check if we find them again while iteration continues. While checking if we find them again, we maintain a single_element object/variable which stores that single element, eventually returning the single_element.
    ii) The other way is to maintain a num_frequency hashmap/dictionary and iterate over it to find which has exactly 1 frequency and return that key/num.
    Time: O(n) for iterating over the nums array
    Space: O(n) for hashing

    Use Xor/Bit Manipulation
    Intuition:
    Xor of any two num gives the difference of bit as 1 and same bit as 0.
    Thus, using this we get 1 ^ 1 == 0 because the same numbers have same bits.
    So, we will always get the single element because all the same ones will evaluate to 0 and 0^single_number = single_number.
    Time: O(n)
    Space: O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num

        return xor
'''

'''
REPL test:

>>> n = 2
>>> m = 2
>>> o = 3
>>> n ^ m
0
>>> n ^ o
1
>>> n ^ m ^ o
3
>>> n ^ o ^ m
3
>>> l = 0
>>> l ^ n ^ o ^ m
3
>>>





'''



class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
