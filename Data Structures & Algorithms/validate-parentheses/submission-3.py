class Solution:
    def isValid(self, s: str) -> bool:

        # while '()' in s or '[]' in s or '{}' in s:
        #     s = s.replace('()', '')
        #     s = s.replace('[]', '')
        #     s = s.replace('{}', '')
        # return s == ''


        closed = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char not in closed:
                stack.append(char)
            else:
                if stack and stack[-1] == closed[char]:
                    stack.pop()
                else: return False
                
        if stack:
            return False
        else:
            return True


            
            














        

