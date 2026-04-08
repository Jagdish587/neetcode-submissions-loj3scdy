class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        final_result = []
        result = Counter(nums).most_common(k)
        for value in result:
            number, frequency = value
            final_result.append(number)
        return final_result

        