class Solution:
    def isValid(self, s: str) -> bool:

        # while '()' in s or '[]' in s or '{}' in s:
        #     s = s.replace('()', '')
        #     s = s.replace('[]', '')
        #     s = s.replace('{}', '')
        # return s == ''



        closed = {')':'(' , '}':'{' , ']':'['}
        stack = []

        for char in s:
            if char in closed:
                # if stack not empty and top of the stack matches the opening paranthesis
                if stack and stack[-1] == closed[char]:
                    stack.pop()
                else:
                    return False
            else: # an opening bracket
                stack.append(char)
        if stack:
            return False
        else:
            return True

