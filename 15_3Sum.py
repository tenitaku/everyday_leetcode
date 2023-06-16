"""
given an array nums and return [a, b, c] that nums[a] + nums[b] + nums[c] = 0
return ans doesn't contain duplicate pair of nums.

sort nums ... O(nlogn)
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]:
                continue

            left, right = index + 1, len(nums) - 1
            while left < right:
                curSum = value + nums[left] + nums[right]
                if curSum < 0:
                    left += 1
                elif curSum > 0:
                    right -= 1
                else:
                    res.append([value, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1 
                    #this is for such an example...[-2(index), -2, 0(left), 0, 2, 2(right)]

        return res
    
sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
