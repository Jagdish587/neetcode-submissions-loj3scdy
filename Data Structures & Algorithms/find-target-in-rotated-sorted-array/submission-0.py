class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left_index = 0
        right_index = len(nums) - 1

        while left_index < right_index:
            mid_index = (left_index + right_index) // 2
            if nums[mid_index] > nums[right_index]:
                left_index = mid_index + 1
            else:
                right_index = mid_index
        pivot =  left_index

        index = self.binary_search(nums, 0, pivot-1, target)
        if index == -1:
            index = self.binary_search(nums, pivot, len(nums) - 1, target)
        
        return index

    def binary_search(self, nums, left_index, right_index, target):
        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2
            if nums[mid_index] == target:
                return mid_index
            if target > nums[mid_index]:
                left_index = mid_index + 1
            else:
                right_index = mid_index - 1
        return -1