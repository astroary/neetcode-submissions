class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left, maxA, right = 0, 0, len(heights) -1

        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            maxA = max(maxA, area)

            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
        return maxA