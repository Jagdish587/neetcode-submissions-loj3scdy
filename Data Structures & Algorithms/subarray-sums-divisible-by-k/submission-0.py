from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        current_sum = 0
        count = 0

        for val in nums:
            current_sum =  current_sum + val
            rem = current_sum % k

            count += seen[rem]

            seen[rem] += 1

        return count 