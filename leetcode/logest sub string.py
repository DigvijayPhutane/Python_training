'''a = input("enter the string: ")
substring = []
for i in a:
    if i in substring:
        pass
    else:
        substring.append(i)

print(substring)
print(len(substring))'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = []  # List to store the current substring without repeating characters
        max_length = 0  # Variable to store the maximum length of the substring

        for char in s:
            if char in substring:
                # Repeating character found, update the substring and check its length
                max_length = max(max_length, len(substring))
                # Remove the elements before the repeating character
                substring = substring[substring.index(char) + 1:]

            # Add the current character to the substring
            substring.append(char)

        # Check the length of the last substring
        max_length = max(max_length, len(substring))

        return max_length

    '''Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104'''