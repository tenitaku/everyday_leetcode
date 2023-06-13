"""
given an num array and return warmerarray
warmerArray[i] = i is the day you wait for next day that temp is higher than nums[i]
if there is no day warmer, return 0 alternative.

time: O(n)
space: O(n)
"""

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        stack = [] # temp : index
        ans = [0] * len(temperatures)

        for i, t in enumerate(temperatures):

            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                print(stackT, stackInd)
                ans[stackInd] = i - stackInd

            stack.append([t, i])
        
        return ans
    
sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))
    
