class Solution:
    def addTwoNumbers(l1, l2):
        ans = []
        if len(l1) > len(l2): l2 = [0] * (len(l1) - len(l2)) + l2
        else: l1 = [0] * (len(l2) - len(l1)) + l1
        for i in range(len(l1)):
            ans.append(l1[-1-i] + l2[-1-i])
        for i in range(len(ans) - 1):
            if ans[i] >= 10:
                ans[i] -= 10
                ans[i+1] += 1
        print(ans)
        if ans[-1] >= 10:
            ans[-1] -= 10
            ans.append(1)
        return ans
    
    print(addTwoNumbers([2,4,3], [5,6,4]))