from collections import deque

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mydequeu = deque(nums)
        mydequeu.rotate(k)
        nums[:] = list(mydequeu)
        