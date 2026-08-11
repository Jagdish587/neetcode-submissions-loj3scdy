from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        current_sum = 0
        count = 0

        for val in nums:
            current_sum += val

            count += seen[current_sum-k]

            seen[current_sum] = seen[current_sum] + 1

        return  count
