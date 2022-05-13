# Given a string s, find the length of the longest substring without repeating characters.
#
#
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#

# incomplete answer
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = ''
        left = 0
        right = 0
        length = max(len(tmp), right - left)
        for i in range(len(s)):
            # if current char not in tmp string, add to it
            if s[i] not in tmp:
                tmp += s[i]
            else:
                # find the next char that is not repeating
                while left <= i:
                    if s[left] == s[i]:
                        left += 1
                        break
                    left += 1
                tmp = s[left:i]
            right += 1
            length = max(len(tmp), right - left)
        return length

# instead of using a string to store the used characters
# we can explore using dictionary to store the used characters and their index
# but I was not able to figure it out...so I turned to the discussion board

# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1731/A-Python-solution-85ms-O(n)
# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/347818/Python3%3A-sliding-window-O(N)-with-explanation
# indext    0    1    2    3   4   5   6   7
# string    a    c    b    d   b   a   c   d
#           ^                  ^
#           |                  |
# 		left               right
# 		seen = {a : 0, c : 1, b : 2, d: 3}
# 		# case 1: seen[b] = 2, current window  is s[0:4] ,
# 		#        b is inside current window, seen[b] = 2 > left = 0. Move left pointer to seen[b] + 1 = 3
# 		seen = {a : 0, c : 1, b : 4, d: 3}
# indext    0    1    2    3   4   5   6   7
# string    a    c    b    d   b   a   c   d
# 						 ^   ^
# 					     |   |
# 				      left  right
# indext    0    1    2    3   4   5   6   7
# string    a    c    b    d   b   a   c   d
# 					     ^       ^
# 					     |       |
# 				       left    right
# 		# case 2: seen[a] = 0,which means a not in current window s[3:5] , since seen[a] = 0 < left = 3
# 		# we can keep moving right pointer.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        max_len = 0
        used_dict = {}
        for i in range(len(s)):
            if s[i] in used_dict and start <= used_dict[s[i]]:
                start = used_dict[s[i]] + 1
            else:
                max_len = max(max_len, i - start + 1)

            used_dict[s[i]] = i

        return max_len

'''
C++ solution
https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/376363/CPP-Solution-for-beginners-or-O(n)-time-or-Longest-Substring-without-repeating-characters


//A solution for beginners, which is straightforward, easy to understand, without too many complications and room to optimize once you understand the basic premise of the question. Hope this helps!

//Time Complexity: O(n)
//Space Complexity: O(min of a,b) for the unordered set. a, is the upper bound of the space complexity.
//Where a: Size of the string
//b: Size of the number of characters in the character-set

class Solution {
public:
	int lengthOfLongestSubstring(string s)
	{
		unordered_set<char> set;

		int i = 0, j = 0, n = s.size(), ans = 0;

		while( i<n && j<n)
		{
			if(set.find(s[j]) == set.end()) //If the character does not in the set
			{
				set.insert(s[j++]); //Insert the character in set and update the j counter
				ans = max(ans, j-i); //Check if the new distance is longer than the current answer
			}
			else
			{
				set.erase(s[i++]);
				/*If character does exist in the set, ie. it is a repeated character,
				we update the left side counter i, and continue with the checking for substring. */
			}
		}

		return ans;
	}
};


'''

'''
Java solution
https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1729/11-line-simple-Java-solution-O(n)-with-explanation

the basic idea is, keep a hashmap which stores the characters in string as keys and their positions as values, and keep two pointers which define the max substring. move the right pointer to scan through the string , and meanwhile update the hashmap. If the character is already in the hashmap, then move the left pointer to the right of the same character last found. Note that the two pointers can only move forward.

   public int lengthOfLongestSubstring(String s) {
        if (s.length()==0) return 0;
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        int max=0;
        for (int i=0, j=0; i<s.length(); ++i){
            if (map.containsKey(s.charAt(i))){
                j = Math.max(j,map.get(s.charAt(i))+1);
            }
            map.put(s.charAt(i),i);
            max = Math.max(max,i-j+1);
        }
        return max;
    }

'''
