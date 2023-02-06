from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        h = min(height[l], height[r])
        s = (r-l) * h
        search_left = True
        while l <= r:
            if search_left:
                l += 1
                if height[l] >= height[r]:
                    search_left = False
                s = max(s, (r-l) * min(height[l], height[r]))
            else:
                r -= 1
                if height[r] >= height[l]:
                    search_left = True
                s = max(s, (r-l) * min(height[l], height[r]))
        search_left = False
        l = 0
        r = n-1
        while l <= r:
            if search_left:
                l += 1
                if height[l] >= height[r]:
                    search_left = False
                s = max(s, (r-l) * min(height[l], height[r]))
            else:
                r -= 1
                if height[r] >= height[l]:
                    search_left = True
                s = max(s, (r-l) * min(height[l], height[r]))
        return s