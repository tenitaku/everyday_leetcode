'''
problem that given nums and return if nums contains duplicate number.
(given a list of numbers, the task is to determine if the list contains a duplicate number. by chatGPT)
code that solve this problem is...
'''

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
    
"""
using hashset, we can run this code. time complexity is O(n), and space complexity is O(n), n is the length of nums.
if we want to test cases, coding like....↓
"""

sol = Solution()
nums = [1, 2, 3, 4, 5, 6]
print(sol.containsDuplicate(nums))