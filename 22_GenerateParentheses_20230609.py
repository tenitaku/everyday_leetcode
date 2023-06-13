"""
given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
example..
n = 3
return ["((()))","(()())","(())()","()(())","()()()"]

using stack 
time: O(n)
space: O(n)
"""

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        ans = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                ans.append("".join(stack))
                return 
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                print(stack)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                print(stack)
                stack.pop()

        backtrack(0, 0)
        return ans
    
sol = Solution()
print(sol.generateParenthesis(3))