class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = list(s)
        for parenthese in parentheses:
            if parenthese == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop(-1)
                else:
                    return False

            elif parenthese == ']':
                if len(stack) != 0 and stack[-1] == '[':
                    stack.pop(-1)
                else:
                    return False

            elif parenthese == '}':
                if len(stack) != 0 and stack[-1] == '{':
                    stack.pop(-1)
                else:
                    return False
            
            else:
                stack.append(parenthese)
        
        if len(stack) == 0:
            return True
        else:
            return False