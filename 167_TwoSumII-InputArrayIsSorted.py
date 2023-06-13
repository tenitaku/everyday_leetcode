"""
given an already sorted array nums, 
and return [index of a + 1, index of b + 1] that nums[a]+nums[b] == target.
must use only constant extra space.

using two pointer left and right...
time: O(n)
space: O(1)
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        left, right = 0, len(nums) - 1

        while left < right:
            cursum = nums[left] + nums[right]
            if cursum == target:
                return [left + 1, right + 1]
            elif cursum > target:
                right -= 1
            else: 
                left += 1
        
        return []
    
sol = Solution()
print(sol.twoSum([2,7,11,15], 9))

