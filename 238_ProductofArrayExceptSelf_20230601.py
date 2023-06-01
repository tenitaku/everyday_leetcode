"""
given an integer array nums, return an array answer such that answer[i] = product of all the elements of nums except nums[i]
example...
nums = [1, 2, 3, 4]
answer = [24(2*3*4), 12(1*3*4), 8(1*2*4), 6(1*2*3*4)]

using prefix ans postfix....
example...
[1, 2, 3, 4]
prefix is 1,[1, 2, 6, 24]
postfix is [24, 24, 12, 4], 1
and ans[i] = prefix[i-1] * postfix[i+1]

but space : O(2N) so not using any space
for loop and for loop 
and directly multiple these duplicate.
time : O(n) and space : O(1)
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        ans = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
            
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]

        return ans
    
sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))



            



        