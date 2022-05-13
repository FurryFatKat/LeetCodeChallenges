# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
#
#
# Example 1:
#
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
#
# Example 2:
#
# Input: s = "God Ding"
# Output: "doG gniD"

# 52 ms, 14.8 MB
# my first take does not comply with the two pointer methodology
class Solution:
    def reverseWords(self, s: str) -> str:
        output = ''
        s_list = s.split()
        for word in s_list:
            output += word[::-1] + ' '

        return output[:-1]

# 109 ms, 14.8 MB
# reverse counting, inspired by DBabichev's reverse string solution
class Solution:
    def reverseWords(self, s: str) -> str:
        output = ''
        s_list = s.split()
        for word in s_list:
            for i in range(len(word)):
                output += word[-i-1]
            output += ' '

        return output[:-1]

# 75 ms, 14.6 MB
# a truly two pointer solution by michaelkareev
# https://leetcode.com/problems/reverse-words-in-a-string-iii/discuss/1051657/Python-3%3A-Two-pointer-approach-(for-the-sake-of-practice)
class Solution3:
    def reverseWords(self, s: str) -> str:
        output = ''
        l, r = 0, 0
        while r < len(s):
            if s[r] != ' ':
                r += 1
            else:
                output += s[l:r+1][::-1]
                r += 1
                l = r
        output += ' '
        r += 1
        output += s[l:r+1][::-1]

        return output[1:]

'''
C++ solution by alexander
https://leetcode.com/problems/reverse-words-in-a-string-iii/discuss/101906/C%2B%2B-Java-Clean-Code

class Solution {
public:
    string reverseWords(string s) {
        for (int i = 0; i < s.length(); i++) {
            if (s[i] != ' ') {   // when i is a non-space
                int j = i;
                for (; j < s.length() && s[j] != ' '; j++) { } // move j to the next space
                reverse(s.begin() + i, s.begin() + j);
                i = j - 1;
            }
        }

        return s;
    }
};



C++ solution by rajat_gupta_
https://leetcode.com/problems/reverse-words-in-a-string-iii/discuss/842597/4-wayseasy-understandingc%2B%2Bfaster

//1.[runtime beats 52.56 %]
class Solution {
public:
    string reverseWords(string s) {
        string result,word;
        for(int i=0;i<s.length();i++){
            if(s[i]!=' '){
                word+=s[i];
            }else{
                reverse(word.begin(),word.end());
                result+=(word);
                result+=" ";
                word.clear();
            }
        }
        reverse(word.begin(),word.end());
        result+=word;
        return result;
    }
};
//2.[faster than 94.78% ]
class Solution {
public:
    string reverseWords(string s) {
        if(s.size()==0) return "";
        stringstream ss(s);
        string word;
        string res="";
        while(ss>>word){
            reverse(word.begin(),word.end());
            res+=word;
            res+=" ";
        }
        res.erase(res.size() - 1);
        //or  res.erase(std::prev(res.end())); [faster one]
        //or  res.resize(res.size() - 1);
        //or  res.pop_back();
        return res;
    }
};
//3.[runtime beats 81.51 % ]
class Solution {
public:
    string reverseWords(string s) {
        if(s.size()<=1) return s;
        int i=0,j,len=s.size();
        while(i<len){
            j=i+1;
            while(s[j]!=' ' && j<len)  j++;
            reverse(s.begin()+i,s.begin()+j);
            i=j+1;
        }
        return s;
    }
};
//4.[faster than 94.66% ]
class Solution {
public:
    string reverseWords(string s) {
        int i = 0;
        for (int j = 0; j < s.size(); ++j) {
            if (s[j] == ' ') {
                reverse(s.begin() + i, s.begin() + j);
                i = j + 1;
            }
        }
        reverse(s.begin() + i, s.end());
        return s;
    }
};





'''
