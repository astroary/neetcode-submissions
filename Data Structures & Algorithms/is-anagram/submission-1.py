class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if len(s) != len(t):
        #     return False
        
        # cS = {} # tracking alphabet count

        # # get count for letters in s
        # for char in s:
        #     # u found a letter and increment its counter
        #     cS[char] = 1 + cS.get(char, 0)

        # #subtract with letters from t
        # for char in t:
        #     # means letter not there or t has more of that alphabet than s
        #     if char not in cS or cS[char] == 0:
        #         return False
        #     cS[char] -= 1

        # return True

        # if len(s) != len(t):
        #     return False
        # count = {}
        # for char in s:
        #     count[char] = 1 + count.get(char, 0)
        # for char in t:
        #     if char not in count or count[char] == 0:
        #         return False
        #     count[char] -= 1
        # return True

        if len(s) != len(t):
            return False
        s1c, s2c = {}, {}
        for char in s:
            s1c[char] = 1 + s1c.get(char, 0)
        for char in t:
            s2c[char] = 1 + s2c.get(char, 0)
        if s1c == s2c:
            return True
        else:
            return False
        