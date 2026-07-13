class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        count = 0
        last_end = intervals[0][1]


        for interval in intervals[1:]:
            if interval[0] < last_end:
                count = count + 1
                last_end = min(interval[1], last_end)
            else:
                last_end = interval[1]
        
        return count