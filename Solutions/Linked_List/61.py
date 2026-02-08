"""
LeetCode 61. Rotate List
Difficulty: Medium
Category: Linked_Lis

Approach:
- (tail.next = head), and find the position to (temp.next = None)
- Time: O(n)
- Space: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next

        k = k % length
        if k == 0:
            return head

        tail.next = head

        ans = head
        temp = head
        for i in range(length - k):
            ans = ans.next
        for i in range(length - k - 1):
            temp = temp.next
        temp.next = None
        return ans