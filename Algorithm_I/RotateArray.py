# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
# Example 2:
#
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# Follow up:
#
#     Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
#     Could you do it in-place with O(1) extra space?



class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums2 = nums.copy()
        length = len(nums)

        # covering a corner case
        if k > length:
            k = abs(k % length)
        # re-arrange the array
        for i in range(length):
            try:
                nums[k] = nums2[i]
                k += 1
            except:
                # when we enter the error state, we must still operate
                # on the array, otherwise we will miss a step
                k = 0
                nums[k] = nums2[i]
                k += 1

# I came up with the above solution after the first submission failed
# due to a corner case, where K, the rotation number is longer than
# the array itself
# 378 ms, 25.4 MB

# 296 ms, 25.4 MB
# Second time going through the study plan
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)

        # covering a corner case
        if k > length:
            k = abs(k % length)
        res = nums.copy()
        for i in range(len(nums)):
            nums[i] = res[-k+i]

# solution explanation from 'user3284'
# https://leetcode.com/problems/rotate-array/discuss/269948/4-solutions-in-python-(From-easy-to-hard)
# Approach #1
#
# varaible previous to store the number being replaced.

class Solution1:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            previous = nums[-1] #initiate a first previous
            for i in range(len(nums)):
                temp = nums[i] #hodl nums[i]
                nums[i] = previous #overwrite the current index
                previous = temp #swap the value
        logging.debug(f"nums: {nums}")

# Complexity Analysis
#
#     Time complexity : O( n∗k). All the numbers are shifted by one step(O (n)O(n)) k times(O (k)O ( k ) ).
#     Space complexity : O(1). No extra space is used.

# Approch #2 Using Extra Array
#
# We use an extra array in which we place every element of the array at its correct position i.e. the number at index ii in the original array is placed at the index (i+k)%(length of array)(i+k). Then, we copy the new array to the original one.

class Solution2:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a = [0] * len(nums)
        for i in range(len(nums)):
            a[(i+k)%len(nums)] = nums[i] #recycle

        for i in range(len(nums)):
            nums[i] = a[i]

# Complexity Analysis
#
#     Time complexity : O(n). One pass is used to put the numbers in the new array. And another pass to copy the new array to the original one.
#     Space complexity :O*(*n). Another array of the same size is used.

# Approach #3 Using Cyclic Replacements
#
# solution 3

class Solution3:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        count = 0
        start = 0
        while count < len(nums):
            current = start
            prev = nums[start] #store the value in the position

            while True:
                next = (current + k) % len(nums) #
                temp = nums[next] #store it temporaly
                nums[next] = prev #overide the next
                prev = temp #reset prev
                current = next #reset current
                count += 1

                if start == current:
                    break

            start += 1
#
# Complexity Analysis
#
#     Time complexity : O(n). Only one pass is used.
#     Space complexity : O(1). Constant extra space is used.

# Approach #4 Using Reverse
#
# Algorithm
#
# This approach is based on the fact that when we rotate the array k times, k%nk elements from the back end of the array come to the front and the rest of the elements from the front shift backwards.
#
# In this approach, we firstly reverse all the elements of the array. Then, reversing the first k elements followed by reversing the rest n-kn−kelements gives us the required result.
#
# Let n=7n=7 and k=3k=3.
#
# Original List                   : 1 2 3 4 5 6 7
# After reversing all numbers     : 7 6 5 4 3 2 1
# After reversing first k numbers : 5 6 7 4 3 2 1
# After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result

class Solution4:
    def rotate(self, nums, k) -> None:
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0, k-1)
        self.reverse(nums,k, len(nums)-1)

    def reverse(self, nums, start, end) -> None:
        """
        :type nums: List[int]
        :type start: int
        :type end: int
        :rtype: None
        """
        while start < end: #
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

# Complexity Analysis
#
#     Time complexity : O(n) .nnelements are reversed a total of three times.
#     Space complexity : O(1). No extra space is used.
#


'''
C++ Solution by zhukov

https://leetcode.com/problems/rotate-array/discuss/54277/Summary-of-C%2B%2B-solutions


#1. Make an extra copy and then rotate.
Time complexity: O(n). Space complexity: O(n).

    class Solution
    {
    public:
        void rotate(int nums[], int n, int k)
        {
            if ((n == 0) || (k <= 0))
            {
                return;
            }

            // Make a copy of nums
            vector<int> numsCopy(n);
            for (int i = 0; i < n; i++)
            {
                numsCopy[i] = nums[i];
            }

            // Rotate the elements.
            for (int i = 0; i < n; i++)
            {
                nums[(i + k)%n] = numsCopy[i];
            }
        }
    };

#2. Start from one element and keep rotating until we have rotated n different elements.
Time complexity: O(n). Space complexity: O(1).

    class Solution
    {
    public:
        void rotate(int nums[], int n, int k)
        {
            if ((n == 0) || (k <= 0))
            {
                return;
            }

            int cntRotated = 0;
            int start = 0;
            int curr = 0;
            int numToBeRotated = nums[0];
            int tmp = 0;
            // Keep rotating the elements until we have rotated n
            // different elements.
            while (cntRotated < n)
            {
                do
                {
                    tmp = nums[(curr + k)%n];
                    nums[(curr+k)%n] = numToBeRotated;
                    numToBeRotated = tmp;
                    curr = (curr + k)%n;
                    cntRotated++;
                } while (curr != start);
                // Stop rotating the elements when we finish one cycle,
                // i.e., we return to start.

                // Move to next element to start a new cycle.
                start++;
                curr = start;
                numToBeRotated = nums[curr];
            }
        }
    };

#3. Reverse the first n - k elements, the last k elements, and then all the n elements.
Time complexity: O(n). Space complexity: O(1).

    class Solution
    {
    public:
        void rotate(int nums[], int n, int k)
        {
            k = k%n;

            // Reverse the first n - k numbers.
            // Index i (0 <= i < n - k) becomes n - k - i.
            reverse(nums, nums + n - k);

            // Reverse tha last k numbers.
            // Index n - k + i (0 <= i < k) becomes n - i.
            reverse(nums + n - k, nums + n);

            // Reverse all the numbers.
            // Index i (0 <= i < n - k) becomes n - (n - k - i) = i + k.
            // Index n - k + i (0 <= i < k) becomes n - (n - i) = i.
            reverse(nums, nums + n);
        }
    };

#4. Swap the last k elements with the first k elements.
Time complexity: O(n). Space complexity: O(1).

class Solution
{
public:
    void rotate(int nums[], int n, int k)
    {
        for (; k = k%n; n -= k, nums += k)
        {
            // Swap the last k elements with the first k elements.
            // The last k elements will be in the correct positions
            // but we need to rotate the remaining (n - k) elements
            // to the right by k steps.
            for (int i = 0; i < k; i++)
            {
                swap(nums[i], nums[n - k + i]);
            }
        }
    }
};

#5. Keep swapping two subarrays.
Time complexity: O(n). Space complexity: O(1).

class Solution
{
public:
    void rotate(int nums[], int n, int k)
    {
        if ((n == 0) || (k <= 0) || (k%n == 0))
        {
            return;
        }

        k = k%n;
        // Rotation to the right by k steps is equivalent to swapping
        // the two subarrays nums[0,...,n - k - 1] and nums[n - k,...,n - 1].
        int start = 0;
        int tmp = 0;
        while (k > 0)
        {
            if (n - k >= k)
            {
                // The left subarray with size n - k is longer than
                // the right subarray with size k. Exchange
                // nums[n - 2*k,...,n - k - 1] with nums[n - k,...,n - 1].
                for (int i = 0; i < k; i++)
                {
                    tmp = nums[start + n - 2*k + i];
                    nums[start + n - 2*k + i] = nums[start + n - k + i];
                    nums[start + n - k + i] = tmp;
                }

                // nums[n - 2*k,...,n - k - 1] are in their correct positions now.
                // Need to rotate the elements of nums[0,...,n - k - 1] to the right
                // by k%n steps.
                n = n - k;
                k = k%n;
            }
            else
            {
                // The left subarray with size n - k is shorter than
                // the right subarray with size k. Exchange
                // nums[0,...,n - k - 1] with nums[n - k,...,2*(n - k) - 1].
                for (int i = 0; i < n - k; i++)
                {
                    tmp = nums[start + i];
                    nums[start + i] = nums[start + n - k + i];
                    nums[start + n - k + i] = tmp;
                }

                // nums[n - k,...,2*(n - k) - 1] are in their correct positions now.
                // Need to rotate the elements of nums[n - k,...,n - 1] to the right
                // by k - (n - k) steps.
                tmp = n - k;
                n = k;
                k -= tmp;
                start += tmp;
            }
        }
    }
};







'''
