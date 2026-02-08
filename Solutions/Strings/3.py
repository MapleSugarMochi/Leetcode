"""
LeetCode 3. Longest Substring Without Repeating Characters
Difficulty: Medium
Category: String

Approach:
- Double Loops
- Time: O(n ^ 2)
- Space: O(n)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 1
        lst = list(s)
        if len(lst) == 0:
            return 0
        elif len(lst) == 1:
            return 1
        else:
            for i in range(len(lst) - 1):
                length = 0
                record = {}
                record[lst[i]] = True
                for j in range(i + 1, len(lst)):
                    if record.get(lst[j]) == None:
                        record[lst[j]] = True
                        length += 1
                        longest = max(longest, length + 1)
                    else:
                        record.clear()
                        break
        return longest