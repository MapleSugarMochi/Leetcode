"""
LeetCode 14. Longest Common Prefix
Difficulty: Easy
Category: Strings

Approach:
- Strings to lists of characters. Loop stops when characters dismatch
- Time: O(n * m)
- Space: O(n * m)
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        words = []
        ans = []
        length = 1000
        for word in strs:
            words.append(list(word))
            if length > len(list(word)): length = len(list(word))
        for i in range(length):
            AllSame = True
            CurrentLetter = words[0][i]
            for word in words:
                if CurrentLetter != word[i]: return ''.join(ans)
            ans.append(CurrentLetter)
        return ''.join(ans)