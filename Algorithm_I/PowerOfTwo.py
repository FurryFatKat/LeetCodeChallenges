# Given an integer n, return true if it is a power of two. Otherwise, return false.
#
# An integer n is a power of two, if there exists an integer x such that n == 2x.
#
#
#
# Example 1:
#
# Input: n = 1
# Output: true
# Explanation: 20 = 1
#
# Example 2:
#
# Input: n = 16
# Output: true
# Explanation: 24 = 16
#
# Example 3:
#
# Input: n = 3
# Output: false

# The methodology here is to count the number of 1's in
# a binary string.

# it should only have 1

# however, negative number will also return true,
# so n > 0 is a must

# 54 ms, 13.8 MB

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return True if bin(n).count('1') == 1 and n > 0 else False



'''
https://leetcode.com/problems/power-of-two/discuss/1638707/PythonC%2B%2BJava-Detailly-Explain-Why-n-and-n-1-Works-oror-1-Line-oror-100-Faster-oror-Easy

    Key Idea
        the binary form of every power of two likes 0b100...0, because pow(2, n) == 1 << n

    1 = 0b1
    2 = 0b10
    4 = 0b100
    8 = 0b1000
    ...

        the binary form of everypow(2, n) - 1 likes0b11..1

    1 - 1 = 0 = 0b0        =>  1 & 0 = 0b1    & 0b0    = 0
    2 - 1 = 1 = 0b1        =>  2 & 1 = 0b10   & 0b1    = 0
    4 - 1 = 3 = 0b11       =>  4 & 3 = 0b100  & 0b11   = 0
    8 - 1 = 7 = 0b111      =>  8 & 7 = 0b1000 & 0b111  = 0
    ...

        so we can find pow(2, n) & (pow(2, n) - 1) == 0
            for example, num = 4 = 0b100
                4 - 1 = 3 = 0b11
                4 & 3 = 0b100 & 0b11 = 0
                Amazing, right?
        But that's not enough! We need to expain that if n is not a power of two then n & n - 1 != 0
            If m is not a power of two, then the binary form of m contains more than one 1, that is 0b1x..x10..0, x represents 0 or 1
                som - 1 = 0b1x..x10..0 - 1 = 0b1x..x01..1, that is the first 1 in m is still in the binary form of m - 1, so that m & (m - 1) = 0b1x..x0..0 > 0
                for example, m = 6 = 0b110
                    6 - 1 = 5 =0b101
                    6 & 5 = 4 =0b100 > 0
                    Did you find it? The bold 1 is still there!!!
        More generally, for any number n > 0
            n & n - 1 removes the last 1 in the binary form of n
            if and only if n is a power of two, there is only one 1 in the binary form of n

If you have any question, feel free to ask. If you like the solution or the explanation, Please UPVOTE!

Python 98.05% Faster

class Solution(object):
    def isPowerOfTwo(self, n):
        return n and not (n & n - 1)

Java 99.97% Faster

class Solution {
    public boolean isPowerOfTwo(int n) {
        return n > 0 && (n & n - 1) == 0;
    }
}

C++ 100% Faster

class Solution {
public:
    bool isPowerOfTwo(int n) {
        return n > 0 && not (n & n - 1);
    }
};


'''

######

'''

https://leetcode.com/problems/power-of-two/discuss/1638961/C%2B%2BPython-Simple-Solutions-w-Explanation-or-All-Possible-Solutions-Explained

✔️ Solution - I (Recursive)

    If a number is power of two, it can be recursively divided by 2 till it becomes 1
    If the start number is 0 or if any intermediate number is not divisible by 2, we return false

class Solution {
public:
    bool isPowerOfTwo(int n) {
        if(!n) return false;
        if(n == 1) return true;
        return n % 2 == 0 and isPowerOfTwo(n / 2);
    }
};

Python

class Solution:
    def isPowerOfTwo(self, n):
        if n == 0: return False
        return n == 1 or (n % 2 == 0 and self.isPowerOfTwo(n // 2))

Time Complexity : O(logn), where n is the given input number
Space Complexity : O(logn), required for recursive stack

✔️ Solution - II (Iterative)

The same solution as above but done iteratively

C++

class Solution {
public:
    bool isPowerOfTwo(int n) {
        if(n == 0) return 0;
        while(n % 2 == 0)
            n /= 2;
        return n == 1;
    }
};

Python

class Solution:
    def isPowerOfTwo(self, n):
        if n == 0: return False
        while n % 2 == 0:
            n /= 2
        return n == 1

Time Complexity : O(logn), where n is the given input number
Space Complexity : O(1)

✔️ Solution - III (Log2 n)

If n is power of 2, log2(n) will always be integer, or more specifically, the power to which 2 must be raised to get n. Thus we only need to check if result of log2(n) is an integer or not.

C++

class Solution {
public:
    bool isPowerOfTwo(int n) {
        return n && log2(n) == trunc(log2(n));
    }
};

Python

class Solution:
    def isPowerOfTwo(self, n):
        return n > 0 and log2(n) == trunc(log2(n))

Time Complexity : O(logn)
Space Complexity : O(1)

✔️ Solution - IV (Pattern in Power of 2)

If a number is a power of 2, we can observe that it will always have just a single set bit in its binary representation. So, we can just count number of set bits and determine if n is power of 2 or not from that.

C++

class Solution {
public:
    bool isPowerOfTwo(int n) {
        return n > 0 && __builtin_popcount(n) == 1;
		// or: return  n > 0 && popcount(n) == 1;       // since C++20
		// or: return n > 0 && has_single_bit(n);       // since C++20
    }
};

Python

class Solution:
    def isPowerOfTwo(self, n):
        return n > 0 and bin(n).count('1') == 1

Time Complexity : O(logn)
Space Complexity : O(1)

✔️ Solution - V (Bit-Trick)

There's a nice bit-trick that can be used to check if a number is power of 2 efficiently. As already seen above, n will only have 1 set bit if it is power of 2. Then, we can AND (&) n and n-1 and if the result is 0, it is power of 2. This works because if n is power of 2 with ith bit set, then in n-1, i will become unset and all bits to right of i will become set. Thus the result of AND will be 0.

If n is a power of 2:
n    = 8 (1000)
n-1  = 7 (0111)
----------------
&    = 0 (0000)         (no set bit will be common between n and n-1)

If n is not a power of 2:
n    = 10 (1010)
n-1  =  9 (1001)
-----------------
&    =  8 (1000)         (atleast 1 set bit will be common between n and n-1)

C++

class Solution {
public:
    bool isPowerOfTwo(int n) {
        return n > 0 && !(n & (n-1));
    }
};

Python

class Solution:
    def isPowerOfTwo(self, n):
        return n > 0 and n & (n-1) == 0

Time Complexity : O(1)
Space Complexity : O(1)

✔️ Solution - VI (Math)

Only a power of 2 will be able to divide a larger power of 2. Thus, we can take the largest power of 2 for our given range and check if n divides it

C++

class Solution {
public:
    bool isPowerOfTwo(int n) {
        return n > 0 and (1 << 31) % n == 0;
    }
};

Python

class Solution:
    def isPowerOfTwo(self, n):
        return n > 0 and (1 << 31) % n == 0

Time Complexity : O(1)
Space Complexity : O(1)

✔️ Solution - VII (Pre-Compute all powers of 2)

We can simply precompute all powers of 2, store it in hashset and check if n is present in it.

C++

unordered_set<int> powOf2;
auto _ = [](){
    for(int i = 0, n = 1; i < 31; i++, n <<= 1) powOf2.insert(n);
    return 0;
}();
class Solution {
public:
    bool isPowerOfTwo(int n) {
        return powOf2.count(n);
    }
};

Python

pow_of_2 = set(2**i for i in range(31))
class Solution:
    def isPowerOfTwo(self, n):
        return n in pow_of_2

Time Complexity : O(1)
Space Complexity : O(1)
'''
