# Reverse bits of a given 32 bits unsigned integer.
#
# Note:
#
#     Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
#     In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
#
#
#
# Example 1:
#
# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
#
# Example 2:
#
# Input: n = 11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)
# Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.



# Got kicked out of the Algorithm I program again, but
# learning is about gaining knowledge, so I will not finish
# Algorithm I but will finish learning the concepts and
# solving the question

# # It took:
# - looking through discussion board
# - Googling bitwise operation
# - and experimenting in REPL to understand this concept




'''
https://leetcode.com/problems/reverse-bits/discuss/54748/AC-Python-44-ms-solution-bit-manipulation

and below is me testing this concept to understand
what happens at each step

User vladn's explanation:
Let's work on an example. Say, n = 19, which is 00000000000000000000000000010011 in binary, so in the output we should get 11001000000000000000000000000000 in binary, which is 3355443200.
We initialize answer to 0, so in binary it's 32 zeroes. We loop over 32 times, since every integer is gonna have 32 possible 0/1.
1st line in the loop: n & 1, we check if last bit of n is set, is it 1 or 0, ans << 1 we shift all bits that we already have in our answer to the left, so after this shifting the bit on the right is 0, + by using + we set the last bit in the answer to the value that we got in n & 1.
2nd line in the loop we shift bits of our initial number n to the right, since we've already checked the last bit of n, so we just move on to the next bit.

So, in our example, I'm gonna show only first 5 right bits, since other bits are 0.
answer = 0, in binary: 00000000000000000000000000000000
answer << 1 is 00000000000000000000000000000000, n & 1 is 00000000000000000000000000000001
after + operation answer is 00000000000000000000000000000001

answer = 1, in binary: 00000000000000000000000000000001
answer << 1 is 00000000000000000000000000000010, n & 1 is 00000000000000000000000000000001
after + operation answer is 00000000000000000000000000000011

answer = 3, in binary: 00000000000000000000000000000011
answer << 1 is 00000000000000000000000000000110, n & 1 is 00000000000000000000000000000000
after + operation answer is 00000000000000000000000000000110

answer = 6, in binary: 00000000000000000000000000000110
answer << 1 is 00000000000000000000000000001100, n & 1 is 00000000000000000000000000000000
after + operation answer is 00000000000000000000000000001100

answer = 12, in binary: 00000000000000000000000000001100
answer << 1 is 00000000000000000000000000011000, n & 1 is 00000000000000000000000000000001
after + operation answer is 00000000000000000000000000011001

And after that in our example, we'll just shift ** 00000000000000000000000000011001 all the way to the left, which is gonna lead to 11001000000000000000000000000000.

Hope it helps :)


>>> n = 43261596
>>> ans = 0
>>> for i in range(32):
...     ans = (ans << 1) + ( n & 1)
...     n >>= 1
...     print(bin(ans))
...     print(bin(n))
...
0b0
0b1010010100000111101001110
0b0
0b101001010000011110100111
0b1
0b10100101000001111010011
0b11
0b1010010100000111101001
0b111
0b101001010000011110100
0b1110
0b10100101000001111010
0b11100
0b1010010100000111101
0b111001
0b101001010000011110
0b1110010
0b10100101000001111
0b11100101
0b1010010100000111
0b111001011
0b101001010000011
0b1110010111
0b10100101000001
0b11100101111
0b1010010100000
0b111001011110
0b101001010000
0b1110010111100
0b10100101000
0b11100101111000
0b1010010100
0b111001011110000
0b101001010
0b1110010111100000
0b10100101
0b11100101111000001
0b1010010
0b111001011110000010
0b101001
0b1110010111100000101
0b10100
0b11100101111000001010
0b1010
0b111001011110000010100
0b101
0b1110010111100000101001
0b10
0b11100101111000001010010
0b1
0b111001011110000010100101
0b0
0b1110010111100000101001010
0b0
0b11100101111000001010010100
0b0
0b111001011110000010100101000
0b0
0b1110010111100000101001010000
0b0
0b11100101111000001010010100000
0b0
0b111001011110000010100101000000
0b0
>>>

'''


'''
>>> n = 43261596
>>> ans = 0
>>> for i in range(32):
...     ans = (ans << 1) | (n & 1)
...     n >>= 1
...     print(bin(ans))
...     print(bin(n))
...
0b0
0b1010010100000111101001110
0b0
0b101001010000011110100111
0b1
0b10100101000001111010011
0b11
0b1010010100000111101001
0b111
0b101001010000011110100
0b1110
0b10100101000001111010
0b11100
0b1010010100000111101
0b111001
0b101001010000011110
0b1110010
0b10100101000001111
0b11100101
0b1010010100000111
0b111001011
0b101001010000011
0b1110010111
0b10100101000001
0b11100101111
0b1010010100000
0b111001011110
0b101001010000
0b1110010111100
0b10100101000
0b11100101111000
0b1010010100
0b111001011110000
0b101001010
0b1110010111100000
0b10100101
0b11100101111000001
0b1010010
0b111001011110000010
0b101001
0b1110010111100000101
0b10100
0b11100101111000001010
0b1010
0b111001011110000010100
0b101
0b1110010111100000101001
0b10
0b11100101111000001010010
0b1
0b111001011110000010100101
0b0
0b1110010111100000101001010
0b0
0b11100101111000001010010100
0b0
0b111001011110000010100101000
0b0
0b1110010111100000101001010000
0b0
0b11100101111000001010010100000
0b0
0b111001011110000010100101000000
0b0
>>>




'''

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # shift everything to the left by one in result
            # and give 1 as value if current field in n is 1
            result = (result << 1) | (n & 1)
            n >>= 1
        return result
