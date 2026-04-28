class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        myset = set()
        left_index = 0
        max_length = 0

        for right_index in range(len(s)):
            while s[right_index] in myset:
                myset.remove(s[left_index])
                left_index = left_index + 1

            myset.add(s[right_index])
            max_length = max(max_length, right_index-left_index+1)
        return max_length
        