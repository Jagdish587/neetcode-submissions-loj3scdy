class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        count = 0
        intial_count = 0
        start_index = 1
        left_index = 0

        for index, value in enumerate(grumpy):
            if value == 0:
                intial_count += customers[index]

        for index, value in enumerate(grumpy[0:minutes]):
            if value == 1:
                count += customers[index]
        max_count = count
        for right_index in range(minutes, len(customers)):
            if grumpy[right_index] == 1:
                count += customers[right_index]
            if grumpy[left_index] == 1:
                count -= customers[left_index]
            max_count = max(max_count, count)
            start_index = start_index + 1
            left_index = left_index + 1
        return max_count + intial_count
        