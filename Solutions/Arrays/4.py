"""
LeetCode 4. Median of Two Sorted Arrays
Difficulty: Hard
Category: Arrays

Approach:
- Binary search on the shorter array
- Time: O(log(m + n))
- Space: O(1)
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): #分割较短的list
            nums1, nums2 = nums2, nums1

        if nums1 == []: #有空list则直接返回num2 median
            if len(nums2) % 2 == 0:
                return (nums2[len(nums2) // 2] + nums2[len(nums2) // 2 - 1]) / 2
            else:
                return nums2[(len(nums2) - 1) // 2]

        m, n = len(nums1), len(nums2)
        left, right = 0, m
        totalLeft = (m + n + 1) // 2

        while left <= right:
            i = (left + right) // 2 #num1分割位置
            j = totalLeft - i #num2分割位置

            L1 = nums1[i-1] if i > 0 else float('-inf') #num1左边最大
            R1 = nums1[i]   if i < m else float('inf') #num1右边最小
            L2 = nums2[j-1] if j > 0 else float('-inf') #num2左边最大
            R2 = nums2[j]   if j < n else float('inf') #num2右边最小

            if L1 <= R2 and L2 <= R1: #左边元素全部比右边元素小时，分割到了median
                if (m + n) % 2 == 1: #奇数个元素
                    return max(L1, L2)
                return (max(L1, L2) + min(R1, R2)) / 2 #偶数个元素

            #调整分割线
            elif L1 > R2: #左边元素比右边大，分割线向左移
                right = i - 1
            else:
                left = i + 1