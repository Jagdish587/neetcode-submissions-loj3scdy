class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        max_freq = 0
        count_freq = defaultdict(int)
        left_index = 0
        max_width = 0

        for right_index in range(len(s)):
            count_freq[s[right_index]] += 1
            max_freq = max(max_freq, count_freq[s[right_index]])
            window_size = right_index - left_index + 1


            while (right_index - left_index + 1) - max_freq > k:
                count_freq[s[left_index]] -= 1
                left_index = left_index + 1
            
            max_width = max(max_width, right_index-left_index+1)
        
        return max_width