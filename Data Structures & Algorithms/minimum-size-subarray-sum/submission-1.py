class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        right_index = 0
        left_index = 0
        min_length = float("inf")
        window_sum = 0

        for right_index in range(len(nums)):
            window_sum += nums[right_index]

            while window_sum >= target:
                width = right_index - left_index + 1
                min_length = min(min_length, width)
                window_sum = window_sum - nums[left_index]
                left_index = left_index + 1
        
        if min_length == float("inf"):
            return 0
        else:
            return min_length