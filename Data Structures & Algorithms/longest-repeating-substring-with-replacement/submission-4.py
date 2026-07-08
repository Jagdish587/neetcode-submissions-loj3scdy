from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left_index = 0
        freq_count_map =  defaultdict(int)
        max_freq = 0
        max_length = 0

        for right_index in range(len(s)):
            freq_count_map[s[right_index]] += 1
            max_freq = max(max_freq, freq_count_map[s[right_index]])

            while (right_index - left_index + 1) - max_freq > k:
                freq_count_map[s[left_index]] -= 1
                left_index = left_index + 1

            max_length = max(max_length, right_index - left_index + 1)
        
        return max_length
