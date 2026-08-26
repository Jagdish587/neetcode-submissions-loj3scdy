class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left_index = 0
        right_index = len(nums)

        while left_index < right_index:
            mid_index = (left_index + right_index) // 2

            if nums[mid_index] >= target:
                right_index = mid_index
            else:
                left_index = mid_index + 1
        
        return left_index