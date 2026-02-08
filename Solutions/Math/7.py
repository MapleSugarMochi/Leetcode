"""
LeetCode 7. Reverse Integer
Difficulty: Medium
Category: Math

Approach:
- Modulo and division
- Time: O(logn)
- Space: O(1)
"""

class Solution:
    def reverse(self, x: int) -> int:
        negative = (x < 0)
        x = abs(x)
        ans = 0
        while x > 0:
            digit = x % 10
            x = int(x / 10)
            ans = ans + digit
            ans = ans * 10
        ans = ans / 10
        if ans < -2 ** 31 or 2 ** 31 - 1 < ans:
            return 0
        if negative:
            return int(0 - ans)
        else:
            return int(ans)