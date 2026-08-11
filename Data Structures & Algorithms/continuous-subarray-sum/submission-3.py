from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = defaultdict(int)
        seen[0] = -1
        current_sum = 0

        for current_index, val in enumerate(nums):
            current_sum += val
            rem = current_sum % k
            if rem in seen:
                length = current_index - seen[rem]
                if length >= 2:
                    return True
            if rem not in seen:
                seen[rem] =  current_index

        return False   

        