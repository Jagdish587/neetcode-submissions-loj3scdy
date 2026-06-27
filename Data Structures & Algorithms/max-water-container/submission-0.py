class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = float("-inf")

        while left < right:
            current_area = (right - left) * min(heights[left], heights[right])
            max_area = max(max_area, current_area)

            if heights[left] <= heights[right]:
                left = left + 1
            else:
                right = right - 1
            
        return max_area