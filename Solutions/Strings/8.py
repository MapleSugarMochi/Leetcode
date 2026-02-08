"""
LeetCode 8. String to Integer (atoi)
Difficulty: Medium
Category: Strings

Approach:
- String to list, and simple operations
- Time: O(n)
- Space: O(n)
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        lst = list(s)
        ans = 0
        positivity = True

        if len(lst) == 0:
            return 0

        if lst[0] == '-':
            positivity = False
            lst.pop(0)
        elif lst[0] == '+':
            positivity = True
            lst.pop(0)

        for digit in lst:
            if not digit.isdigit():
                break
            else:
                ans *= 10
                ans += int(digit)
        
        if ans > 2 ** 31 - 1 and positivity:
            return 2 ** 31 - 1
        elif -ans < -2 ** 31 and not positivity:
            return -2 ** 31
        
        if positivity:
            return ans
        else:
            return -ans