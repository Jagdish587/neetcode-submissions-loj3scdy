class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_width = 0
        left_index = 0
        right_index = 0
        myset = set()

        for right_index in range(len(s)):
            while s[right_index] in myset:
                myset.remove(s[left_index])
                left_index = left_index + 1 

            myset.add(s[right_index])
            max_width = max(max_width, right_index-left_index+1)
        return max_width


        