class Solution:
    def maxProduct(self, nums: List[int]) -> int:


        max_forward = float("-inf")
        max_reverse = float("-inf")
        current_prod = 1

        for value in nums:
            current_prod = current_prod * value
            max_forward = max(max_forward, current_prod)
            if current_prod == 0: 
                current_prod = 1

        current_prod = 1
        for value in reversed(nums):
            current_prod = current_prod * value
            max_reverse = max(max_reverse, current_prod)
            if current_prod == 0: 
                current_prod = 1

        max_prod = max(max_forward, max_reverse)
        return max_prod