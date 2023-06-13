"""
given an string and return if string is a valid palindrome.
string contains , and space. so we should remove those character.

valid palindrome means string and reverse string is the same.
so we can easily solve this problem by return str == str[::-1]
but it takes O(n) time and need more space of O(n)

so we want to solve by O(1)
...so using two pointer left and right..
"""

class Solution:
    def isvalidPalindrome(self, s: str) -> bool:

        left, right = 0, len(s) - 1

        while (left < right):
            while not self.isAlphabetNum(s[left]) and left < right:
                left += 1

            while not self.isAlphabetNum(s[right]) and left < right:
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
    
        return True
    
    def isAlphabetNum(self, c: str) -> bool:
        return (ord("A") <= ord(c) <= ord("Z") 
                or ord("a") <= ord(c) <= ord("z") 
                or ord("0") <= ord(c) <= ord("9"))
    
sol = Solution()
print(sol.isvalidPalindrome("A man, a plan, a canal: Panama"))

