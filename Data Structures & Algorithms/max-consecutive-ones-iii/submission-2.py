class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        zero_count = 0
        left_index = 0
        max_length = 0
        
        for right_index in range(len(nums)):
            if nums[right_index] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left_index] == 0:
                    zero_count -= 1
                left_index = left_index + 1 

            
            max_length = max(max_length, right_index-left_index+1)
        
        return max_length
