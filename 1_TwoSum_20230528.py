"""
given an array of integers nums and an integer target, 
nums = [2, 7, 5] target = 9, return true (nums[0] + nums[1] = 9)
0 + 9 = OK

brute force...double for loop
time : O(n^2)
space : O(1)

using hash map ..... hashmap[val:index]
and for loop search
time : O(n)
space : O(n)
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        hashmap = {} # val : index

        for i, n in enumerate(nums):
            another = target - n
            if another in hashmap:
                return [hashmap[another], i]
            hashmap[n] = i
            
        return []

sol = Solution()
print(sol.twoSum([1, 2, 3, 4, 2, 2], 9))