"""
LeetCode 13. Roman to Integer
Difficulty: Easy
Category: Strings

Approach:
- Loop
- Time: O(n)
- Space: O(n)
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        digits = list(s)
        jump = False
        for i in range(len(digits)):
            if jump:
                jump = False
                continue
            if digits[i] == "V":
                ans = ans + 5
            elif digits[i] == "L":
                ans = ans + 50
            elif digits[i] == "D":
                ans = ans + 500
            elif digits[i] == "M":
                ans = ans + 1000
            
            elif digits[i] == "I":
                if i == len(digits) - 1:
                    ans = ans + 1
                    continue
                if digits[i+1] == "V":
                    ans = ans + 4
                    jump = True
                elif digits[i+1] == "X":
                    ans = ans + 9
                    jump = True
                else:
                    ans = ans + 1
            
            elif digits[i] == "X":
                if i == len(digits) - 1:
                    ans = ans + 10
                    continue
                if digits[i+1] == "L":
                    ans = ans + 40
                    jump = True
                elif digits[i+1] == "C":
                    ans = ans + 90
                    jump = True
                else:
                    ans = ans + 10

            elif digits[i] == "C":
                if i == len(digits) - 1:
                    ans = ans + 100
                    continue
                if digits[i+1] == "D":
                    ans = ans + 400
                    jump = True
                elif digits[i+1] == "M":
                    ans = ans + 900
                    jump = True
                else:
                    ans = ans + 100
        return ans