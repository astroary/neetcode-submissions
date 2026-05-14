class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1c,s2c = {}, {}
        for char in s:
            s1c[char] = 1 + s1c.get(char, 0)
        for char in t:
            s2c[char] = 1 + s2c.get(char, 0)
        if s1c != s2c:
            return False
        else: return True