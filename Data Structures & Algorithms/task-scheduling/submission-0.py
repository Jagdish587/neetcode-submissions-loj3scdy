class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_occurence = max(Counter(tasks).values())
        count_max_occurence = sum(1 for value in Counter(tasks).values() if value == max_occurence)
        min_time = max(len(tasks), (max_occurence - 1) * (n + 1) + count_max_occurence) 
        return min_time
        