class Solution:
    def lengthOfLongestSubstring(self,s):
        char_dict = {}
        max_len = 0
        start = 0 
        
        for x in range(len(s)):
            if s[x] in char_dict:
                start = max(start, char_dict[s[x]]+1)
            char_dict[s[x]] = x
            max_len = max(max_len, x-start + 1)
            
        return max_len