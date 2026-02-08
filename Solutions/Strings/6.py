"""
LeetCode 6. Zigzag Conversion
Difficulty: Medium
Category: Arrays

Approach:
- Iterate row by row and pick characters in the zigzag pattern.
- For middle rows, include the additional character that appears diagonally. Concatenate all characters to form the final converted string
- Time: O(n)
- Space: O(n)
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        a=""
        for i in range(numRows):
            for j in range(i,len(s),2*(numRows-1)):
                a+=s[j]
                if(i>0 and i<numRows-1 and j+2*(numRows-1)-2*i < len(s)):
                    a+=s[j+2*(numRows-1)-2*i]
        return a