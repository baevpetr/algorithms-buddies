# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two Pointers
        l, r = 0, len(height) - 1
        max_area = -1

        while l < r:
            cur_area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, cur_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
