class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        current_sum = nums[0]
        result_sum = nums[0]
        
        for val in nums[1:]:
            current_sum = max(val, current_sum + val)
            result_sum = max(result_sum, current_sum)
        
        return result_sum

        