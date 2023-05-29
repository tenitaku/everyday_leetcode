"""
given an array of strings strs, group the anagrams together.
example....
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
"""
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = defaultdict(list) #mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1  # ord can change char to unicode ("a" == 80)
            
            ans[tuple(count)].append(s)
        
        return ans.values()
"""
さすがに初見では難しかったので日本語で解説
まず、最後に返すdictionaryを作成する、ここではlist型のdictionary
次に、strsの文字を順に走査していく
aからzまで、登場回数を数え、count[c]++していく
最後に、登場回数が同じものの語句をansのvalueのlistに追加する。
ここで気をつけるのは、ans[list(count)].append(s)としても動作しない点である。
tuple(count)を使用する。
理由として、dictionaryのkeyはhashableでなくてはならないからである。（hashableとは変更ができないこと）
listは変更可能なので、かわりにtupleを使用する。
.values()で辞書のvalue一覧を、.keys()で辞書のkey一覧を取得することができる。
"""

sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))