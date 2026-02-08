"""
LeetCode 2. Add Two Numbers
Difficulty: Medium
Category: Linked_List

Approach:
- Simulate column addition
- Time: O(n)
- Space: O(n)
"""

class Solution:
    def addTwoNumbers(self, listnode1: Optional[ListNode], listnode2: Optional[ListNode]) -> Optional[ListNode]:
        
        def to_list(head):
            arr = []
            while head:
                arr.append(head.val)
                head = head.next
            return arr

        def build_list(arr):
            dummy = ListNode()
            cur = dummy
            for x in arr:
                cur.next = ListNode(x)
                cur = cur.next
            return dummy.next

        ans = []
        l1 = to_list(listnode1)
        l2 = to_list(listnode2)
        if len(l1) > len(l2): l2 = l2 + [0] * (len(l1) - len(l2))
        else: l1 = l1 + [0] * (len(l2) - len(l1))
        for i in range(len(l1)):
            ans.append(l1[i] + l2[i])
        for i in range(len(ans) - 1):
            if ans[i] >= 10:
                ans[i] -= 10
                ans[i+1] += 1
        if ans[-1] >= 10:
            ans[-1] -= 10
            ans.append(1)
        return build_list(ans)