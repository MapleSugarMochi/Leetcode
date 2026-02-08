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