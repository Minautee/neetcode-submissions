class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1

        max_amt = 0
        while left < right:
            width = right - left
            length = min(heights[left], heights[right])
            max_amt = max(max_amt, (length * width))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_amt
        