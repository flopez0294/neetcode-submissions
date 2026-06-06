class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            x = ((r - l) * min(heights[l], heights[r]))
            if ((r - l) * min(heights[l], heights[r])) > mx:
                mx = x
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return mx