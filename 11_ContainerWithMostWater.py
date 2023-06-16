"""
given an integer array of heights and return most capable water.
each element in height is equal to height of wall.
image:wall---water---wall

we use two pointer left and right.
O(n)
"""

class Solution:
    def mostWater(self, heights: list[int]) -> int:
        res = 0
        left, right = 0, len(heights) - 1

        while left < right:
            curArea = (right - left) * min(heights[left], heights[right])
            res = max(res, curArea)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return res
    
sol = Solution()
print(sol.mostWater([1,8,6,2,5,4,8,3,7]))
