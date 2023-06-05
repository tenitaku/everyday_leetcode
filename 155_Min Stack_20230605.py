"""
given an array order and num,
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

using two stack, one is stack and another is minstack
"""
class MinStack:

    def __init__(self):
        self.minstack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        curmin = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(curmin)

    def pop(self) -> None:
        del self.stack[-1]
        del self.minstack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]
        else:
            return 0

sol = MinStack()
print(sol.push(-2))
print(sol.push(0))
print(sol.push(-3))
print(sol.getMin())
print(sol.pop())
print(sol.top())
print(sol.getMin())