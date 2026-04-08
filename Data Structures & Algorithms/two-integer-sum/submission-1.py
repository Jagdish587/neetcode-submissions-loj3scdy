class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for index, value in enumerate(nums):
            diff_value = target - value
            if diff_value in result:
                return [result[diff_value],index]
            else:
                result[value] = index
        