class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        left = 0
        right = len(people) - 1

        while left <= right:
            if people[left] + people[right] <= limit:
                left = left + 1
            right = right - 1
            boats = boats + 1
        return boats