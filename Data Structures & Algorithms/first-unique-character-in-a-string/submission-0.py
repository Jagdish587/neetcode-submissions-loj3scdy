class Solution:
    def firstUniqChar(self, s: str) -> int:
        for ch in s:
            if s.count(ch) == 1:
                index_val = s.find(ch)
                return index_val
        return -1
        