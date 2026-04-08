class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        max_length = 0

        nums_set = set(nums)

        for num in nums:
            length = 0
            if(num - 1) not in nums_set:
                while(num + length) in nums_set:
                    length = length + 1
            max_length = max(max_length, length)
        return max_length
            