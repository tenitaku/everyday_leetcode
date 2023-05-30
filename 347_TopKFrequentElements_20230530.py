"""
given an array nums and an integer k, return the k most frequent elements in any order.
example:
nums = [1, 1, 1, 1, 2, 2, 2, 3, 4], k = 2
answer = [1, 2] because 1 and 2 is the most 2 frequent elements
"""

"""
using dict.... [key : value] = [num : count]
answer = [k element]
time : O(n)
space : O(n)
"""

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        count = {} # num : count
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for key, val in count.items():
            freq[val].append(key)

        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans

sol = Solution()
print(sol.topKFrequent([1, 1, 1, 1, 2, 2, 2, 3, 4], 2))