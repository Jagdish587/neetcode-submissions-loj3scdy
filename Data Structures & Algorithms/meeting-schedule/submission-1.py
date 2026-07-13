"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        print("intervals = ", intervals)
        if len(intervals) == 0:
            return True
        intervals.sort(key=lambda x: x.start)
        print("intervals = ", intervals)
        # count = 0
        last_end = intervals[0].end
        print("last_end = ", last_end)

        for interval in intervals[1:]:
            if interval.start < last_end:
                return False
            else:
                last_end = interval.end
        
        return True
        