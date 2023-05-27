"""
ploblem introduction..
given two strings s and t, return true if t is an anagram of s.
(s and t consist of lowercase English letters.)
anagram : a word formed by rearranging the letters. typically using all the original letters exactly once.
let's solve this problem.
"""

"""
memo
(anagram, nagaram) -> true.
aaanrmg aaanrgm
count number of each character...
[a:1]...[z:0]
using hashmap.
time: O(s+t)
space:O(s+t)

sort case....time:O(nlogn), space:O(1)
sort both s and t and return s==t
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #base case
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            # important!
            if countS[c] != countT.get(c, 0):
                return False
            
        return True
    
"""
important!
if S contains c but T doesn't contain c , we should return 0 (default value)..
so we use countT.get(c, 0) instead of countT[c]

test down below
"""
sol = Solution()
print(sol.isAnagram("abbbr", "arbbb"))






