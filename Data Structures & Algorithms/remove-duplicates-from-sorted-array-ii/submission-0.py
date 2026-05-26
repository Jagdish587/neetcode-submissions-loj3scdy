from collections import Counter

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        my_dict = Counter(nums)
        index_pos = 0


        for key,value in my_dict.items():
            iterate_times = min(2, value)

            while iterate_times > 0:
                nums[index_pos] = key
                index_pos = index_pos + 1
                iterate_times = iterate_times - 1
        
        return index_pos
        
        