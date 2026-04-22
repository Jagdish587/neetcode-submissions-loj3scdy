class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        start_index = 0
        for ch in s:
            index_pos = t.find(ch, start_index, len(t))
            if index_pos == -1:
                return False
            start_index = index_pos + 1
        return True
        