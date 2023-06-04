"""
given a string and check if string is valid...
if s = "[[[[[]]]]]"....true
s contains [], {} and ()
if s = "[(])"....false

time : O(n)
space : O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in hashmap:
                if stack and stack[-1] == hashmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

sol = Solution()
print(sol.isValid("()[]{}"))