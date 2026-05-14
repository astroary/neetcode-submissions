class Solution:
    def isValid(self, s: str) -> bool:
        bracks = {')':'(', '}':'{', ']':'['}
        stack = []

        for char in s:
            if char not in bracks:
                stack.append(char)
            else:
                if stack and bracks[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else: return True