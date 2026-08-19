from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq_map = Counter(nums)
        for key, value in freq_map.items():
            if value % 2 != 0:
                return False
        return True
        