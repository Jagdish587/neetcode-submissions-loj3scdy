class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        even_index = 0
        odd_index = 1
        for val in nums:
            if val > 0:
                res[even_index] = val
                even_index = even_index + 2
            else:
                res[odd_index] = val
                odd_index = odd_index + 2
        return res
        