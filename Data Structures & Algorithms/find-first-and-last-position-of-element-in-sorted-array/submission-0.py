class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        if nums:
            res[0] = self.find_first_occurence(nums, target)
            res[1] = self.find_last_occurence(nums, target)
        return res

    def find_first_occurence(self, nums, target):

        left_index = 0
        right_index = len(nums) - 1

        while left_index <= right_index:
            mid_index = (left_index + right_index)//2
            if target <= nums[mid_index]:
                right_index = mid_index - 1
            else:
                left_index = mid_index + 1

        if left_index < len(nums) and nums[left_index] == target:
            return left_index
        return -1



    def find_last_occurence(self, nums, target):

        left_index = 0
        right_index = len(nums) - 1

        while left_index <= right_index:
            mid_index = (left_index + right_index)//2
            
            if target >= nums[mid_index]:
                left_index = mid_index + 1
            else:
                right_index = mid_index - 1

        if right_index >= 0 and nums[right_index] == target:
            return right_index
        return -1