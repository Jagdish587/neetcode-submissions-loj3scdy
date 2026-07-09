class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        initial_customer_count = 0
        max_customers = 0
        window_count = 0

        for index, value in enumerate(grumpy):
            if value == 0:
                initial_customer_count += customers[index]


        for index, value in enumerate(grumpy[0:minutes]):
            if value == 1:
                window_count += customers[index]
    
        max_customers = window_count
        left_index = 0

        for right_index in range(minutes, len(grumpy)):
            if grumpy[right_index] == 1:
                window_count += customers[right_index]

            if grumpy[left_index] == 1:
                window_count -= customers[left_index]
            
            max_customers = max(max_customers, window_count)
            left_index = left_index + 1
        
        return initial_customer_count + max_customers