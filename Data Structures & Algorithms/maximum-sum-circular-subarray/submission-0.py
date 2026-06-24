class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        current_max = 0
        min_sum = 0
        current_min = 0 
        total_sum = sum(nums)   

        for index in range(len(nums)):
            current_max = max(nums[index], current_max+nums[index])
            max_sum = max(max_sum, current_max)


            current_min = min(nums[index], current_min+nums[index])
            min_sum = min(min_sum, current_min)

        if max_sum < 0:
            return  max_sum
         
        return max(max_sum, total_sum-min_sum)
        