class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:


        nums.sort()
        res = []

        for first in range(len(nums)-3):
            if first > 0 and nums[first] == nums[first-1]:
                continue

            for second in range(first+1, len(nums)-2):
                if second > first+1 and nums[second] == nums[second-1]:
                    continue

                left = second + 1
                right = len(nums) - 1

                while left < right:
                    current_sum = nums[first] + nums[second] + nums[left] + nums[right]
                    if current_sum < target:
                        left = left + 1
                    elif current_sum > target:
                        right = right - 1
                    else:
                        res.append([nums[first], nums[second], nums[left], nums[right]])
                        left = left + 1
                        right = right - 1

                        while left < right and nums[left] == nums[left-1]:
                            left = left + 1
                        
                        while left < right and nums[right] == nums[right+1]:
                            right = right - 1 
        
        return res
        