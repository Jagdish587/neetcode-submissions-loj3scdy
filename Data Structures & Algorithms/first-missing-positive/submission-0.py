class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num = 1
        set_val = set(nums)

        while num < float("inf"):
            if num not in set_val:
                return num
            num += 1