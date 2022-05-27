# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.
#
#
#
# Example 1:
#
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
#
# Example 2:
#
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

# https://leetcode.com/problems/permutation-in-string/discuss/1761953/Python3-SLIDING-WINDOW-OPTIMIZED-(-)-Explained
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        cntr, w, match = Counter(s1), len(s1), 0
        print(type(cntr))
        for i in range(len(s2)):
            if s2[i] in cntr:
                if not cntr[s2[i]]:
                    match -= 1
                cntr[s2[i]] -= 1
                if not cntr[s2[i]]:
                    match += 1

            if i >= w and s2[i-w] in cntr:
                if not cntr[s2[i-w]]:
                    match -= 1
                cntr[s2[i-w]] += 1
                if not cntr[s2[i-w]]:
                    match += 1

            if match == len(cntr):
                return True
        return False

'''
C++ Solution

https://leetcode.com/problems/permutation-in-string/discuss/1762469/C%2B%2B-oror-SLIDING-WINDOW-OPTIMIZED-oror-Well-Explained

Let us first redefine the problem.

So permutation of a string basically means just the reordering of the letters of the string. That means all the permutations of a string are just the anagrams of the string, with all the letters included, just in another way.
And we have to find if such a substring exists in s2 which is a permutation of s1, which means we have to find a substring in s2 such that the frequency of the characters in that substring is same as the frequency of the characters in s1.

So we will be using SLIDING WINDOW APPROACH to find such a window in s2 in which the freq of characters is same as s1.

Algorithm:

1. The first step is to find the freq of all characters of s1.

2. Then we will be starting with a window of size 1 initially in s2. That means start=0, end=0.

3. Along with this, we will also be maintaining the frequency of the characters in the current window.

4. We will be continuing the below steps untill we reach a situation where the end of the window reaches the end of s2. That means we will be doing the steps while end<length of s2.
		a) Increase the frequency of the character which is just now newly included inside the window. That means increase the frequency of s2[end].
		b) Now check if the frequency of the characters in the current window, is same as the frequency of characters int s1. But this is only possible if the length of current substring(window) is same as the length of s1. If this is true, then we can directly return true from here.
		c) If the frequency doesnt match, we have to change the window:-
					i) If the length of window in less than the length of s1, then we should increase the length of the the window by increasing the end. So end+=1.
					ii) If not, that means length of window is greater than or equal to the length of s1, so we will need to move to a new window. For that we will have to move start to the next character but before that we will have to decrease the frequency of start character from the curr window frequency. That means
							-Decrese the frequency of s2[start].
							-Move start to the next element.
							-Move end to the next element.

5. If the algorithm did not return true for any window, then we will reach here(out of the loop). This will mean that we did not find any such substring in s2. So return false.


Example:

class Solution {
    bool areVectorsEqual(vector<int> a, vector<int> b){
        for(int i=0; i<26; i++){
            if(a[i]!=b[i]) return false;
        }
        return true;
    }
public:
    bool checkInclusion(string s1, string s2) {
        if(s2.size()<s1.size()) return false;
        vector<int> freqS1(26, 0);
        for(char c: s1) freqS1[c-'a']++;

        vector<int> freqS2(26, 0);
        int i=0, j=0;

        while(j<s2.size()){
            freqS2[s2[j]-'a']++;

            if(j-i+1==s1.size()){
                if(areVectorsEqual(freqS1, freqS2)) return true;
            }

            if(j-i+1<s1.size()) j++;
            else{
                freqS2[s2[i]-'a']--;
                i++;
                j++;
            }
        }
        return false;
    }
};


'''
