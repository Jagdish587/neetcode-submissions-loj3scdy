class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        merged.append(intervals[0])

        for interval in intervals[1:]:

            # overlap case
            if interval[0] <= merged[-1][1]:
                merged[-1][1] = max(interval[1], merged[-1][1])
            else: # no overlap case
                merged.append(interval)
        
        return merged