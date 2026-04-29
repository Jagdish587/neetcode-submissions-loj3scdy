class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        heap_list = []
        for value in arr:
            difference = abs(value - x)
            heapq.heappush(heap_list, (difference, value))
        nsmall_list = heapq.nsmallest(k, heap_list)
        result = [value for diff, value in nsmall_list]
        result.sort()
        return result