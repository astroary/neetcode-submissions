class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1c ,s2c = {}, {}

        for char in s1:
            s1c[char] = 1 + s1c.get(char, 0)
        
        for r in range(len(s2)):
            char_in = s2[r]
            s2c[char_in] = 1 + s2c.get(char_in, 0)
            if r >= len(s1):
                char_out = s2[r-len(s1)]
                if s2c[char_out] == 1:
                    del s2c[char_out]
                else:
                    s2c[char_out]-=1
        
            if s1c == s2c:
                return True
        return False