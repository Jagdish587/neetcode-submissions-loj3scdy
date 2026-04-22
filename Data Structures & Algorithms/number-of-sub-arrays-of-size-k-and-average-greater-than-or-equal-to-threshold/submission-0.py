class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        initial_index = 0
        count = 0
        
        intial_sum_val = sum(arr[:k])
        average = intial_sum_val // k

        if average >= threshold:
            count = 1

        for val in range(k, len(arr)):
            intial_sum_val = (intial_sum_val + arr[val] - arr[initial_index])
            average = intial_sum_val // k
            initial_index = initial_index + 1
            if average >= threshold:
                count += 1
        
        return count