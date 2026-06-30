class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        
        res = []

        nums.sort()

        for index, value in enumerate(nums):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            left = index+1
            right = len(nums)-1

            while left < right:
                current_sum = nums[index] + nums[left] + nums[right]
                if current_sum < 0:
                    left = left + 1
                elif current_sum > 0:
                    right = right - 1
                else:
                    res.append([nums[index],nums[left],nums[right]])
                    left = left + 1
                    right = right - 1

                    # skip duplicate 2nd element
                    while left < right and nums[index] == nums[index-1]:
                        left = left + 1

                    # skip duplicate 3rd element
                    while left < right and nums[right] == nums[right+1]:
                        right = right - 1
        
        return res
        