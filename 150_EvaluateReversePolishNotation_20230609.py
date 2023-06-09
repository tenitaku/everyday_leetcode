"""
given num and operaters(-+/*) and return the answer
example..
tokens = [2, 1, +, 3, *]
return (2+1)*3 = 9

time : O(n)
space : O(n)
"""

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        
        return stack[0]
    
sol = Solution()
print(sol.evalRPN(["2","1","+","3","*"]))
