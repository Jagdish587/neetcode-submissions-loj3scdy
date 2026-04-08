class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_dict = {}
        for index, value in enumerate(numbers):
            difference = target - value
            if difference in my_dict:
                return[my_dict[difference]+1, index+1]
            my_dict[value] = index
        