"""
LeetCode 1. Two Sum
Difficulty: Easy
Category: Array

Approach:
- Double Loops
- Time: O(n ^ 2)
- Space: O(1)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            temp = target - nums[i]
            for j in range(len(nums) - 1 - i):
                if nums[j + i + 1] == temp:
                    return [i,j + i + 1]