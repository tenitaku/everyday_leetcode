"""
given an unsorted array and return len of consecutive elements in an array.
example 
array = [1, 2, 3, 100]
return =  3 (1, 2, 3 is the longest consecutive)
we should code within O(n)

start num doesn't contain (num - 1)
and check len of start to the end
time : O(n)
"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        numset = set(nums)
        maxlen = 0

        for num in nums:
            if (num - 1) not in numset:
                length = 0
                while (num + length) in numset:
                    length += 1
                maxlen = max(maxlen, length)

        return maxlen
    
sol = Solution()
print(sol.longestConsecutive([1, 2, 3, 4, 5, 100]))
