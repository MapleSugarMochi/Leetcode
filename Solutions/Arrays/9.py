"""
LeetCode 9. Palindrome Number
Difficulty: Easy
Category: Arrays

Approach:
- String to list, and simple operations
- Time: O(logn)
- Space: O(logn)
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else: 
            digits = list(str(x))
            for i in range(int(len(digits)/2)):
                if digits[i] != digits[-1 - i]:
                    return False
        return True