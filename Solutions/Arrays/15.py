"""
LeetCode 15. 3Sum
Difficulty: Medium
Category: Arrays

Approach:
- Use 2 pointers to find triplets [currentNumber, p1, p2]. Skip duplicates to avoid repeated answers
- Time: O(n ^ 2)
- Space: O(1)
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for a in range(len(nums)):
            if a > 0 and nums[a] == nums[a - 1]: continue
            if nums[a] > 0: break
            left = a + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] + nums[a] == 0:
                    ans.append([nums[a], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] > 0 - nums[a]:
                    right -= 1
                else:
                    left += 1
        return ans