class Solution:
    def myAtoi(self, s: str) -> int:
        lst = list(s)
        ans = 0

        if len(lst) == 0:
            return 0

        while lst[0] == ' ':
            lst.pop(0)
            if len(lst) == 0:
                return 0

        if (not lst[0].isdigit()) and (not lst[0] == '-') and (not lst[0] == '+'):
            return 0

        if lst[0] == '-':
            positivity = False
            lst.pop(0)
        elif lst[0] == '+':
            positivity = True
            lst.pop(0)
        else:
            positivity = True

        for digit in lst:
            if not digit.isdigit():
                break
            else:
                ans *= 10
                ans += int(digit)
        
        if ans > 2 ** 31 - 1 and positivity:
            return 2 ** 31 - 1
        elif -ans < -2 ** 31 and not positivity:
            return -2 ** 31
        
        if positivity:
            return ans
        else:
            return -ans