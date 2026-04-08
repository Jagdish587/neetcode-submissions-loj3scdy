class MedianFinder:

    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap = []
        

    def addNum(self, num: int) -> None:
        if self.right_min_heap and num > self.right_min_heap[0]:
            heapq.heappush(self.right_min_heap, num)   
        else:
            heapq.heappush(self.left_max_heap, -1 * num)
            
        if len(self.left_max_heap) < len(self.right_min_heap) + 1:
            # pop element from right and insert to left max heap
            val = heapq.heappop(self.right_min_heap)
            heapq.heappush(self.left_max_heap, -1 * val)
        if len(self.left_max_heap) > len(self.right_min_heap) + 1:
            # pop element from left max and insert to right
            val = -1 * heapq.heappop(self.left_max_heap)
            heapq.heappush(self.right_min_heap, val)

    def findMedian(self) -> float:

        if len(self.left_max_heap) == len(self.right_min_heap): # even length
            left_value = -1 * self.left_max_heap[0]
            right_value = self.right_min_heap[0]
            return (left_value + right_value)/2.0
        else:
            if len(self.left_max_heap) > len(self.right_min_heap):
                return (-1 * self.left_max_heap[0])
            else:
                return self.right_min_heap[0]
        
        