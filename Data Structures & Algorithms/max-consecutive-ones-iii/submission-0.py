class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        max_width = 0
        left_index = 0

        for right_index in range(len(nums)):
            if nums[right_index] == 0:
                k = k - 1
            
            while k < 0:
                if nums[left_index] == 0:
                    k = k + 1
                left_index = left_index + 1

            max_width = max(max_width, right_index-left_index+1)
        
        return max_width