class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_result = 0
        left_index = 0
        sum_val = 0
        max_result = nums[0]

        for right_index in range(0, len(nums)):
            sum_val = sum_val + nums[right_index]
            max_result = max(max_result, sum_val)
            while sum_val < 0:
                sum_val = sum_val - nums[left_index]
                left_index = left_index + 1
        return max_result
        