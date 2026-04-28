from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start_index = 0
        right_index = 0
        s1_freq = Counter(s1)

        for right_index in range(len(s1), len(s2)+1):
            window = s2[start_index:right_index]
            print(right_index, window)
            s2_freq = Counter(window)
            if s2_freq == s1_freq:
                return True
            start_index = start_index + 1
        return False

        