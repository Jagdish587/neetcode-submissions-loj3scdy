class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result_array = [1] * len(nums)
        result = 1
        for index, value in enumerate(nums):
            result_array[index] = result
            result = result * value         
        result = 1
        for index in reversed(range(len(nums))):
            result_array[index] = result_array[index] * result
            result = result * nums[index]
        return result_array
                