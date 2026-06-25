class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        current_sum = 0
        prefix_sum_dict = defaultdict(int) # sum : how many times occurred freq
        prefix_sum_dict[0] = 1
        for val in nums:
            current_sum += val
            count += prefix_sum_dict[current_sum-k]
            prefix_sum_dict[current_sum] += 1
        return count