"""
count the num of car fleet.
car fleet means the collision of two cars.
given two array position and speed.
and return the num of collision..
the car catch up front car runs same speed of front car.
"""

class Solution:
    def carfleet(self, target: int, position: list[int], speed: list[int]) -> int:

        stack = []
        pair = [[p, s] for p, s in zip(position, speed)]

        for p, s in sorted(pair)[::-1]:
            stack.append((target - p)/s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
    
sol = Solution()
print(sol.carfleet(12, [10,8,0,5,3], [2,4,1,1,3]))