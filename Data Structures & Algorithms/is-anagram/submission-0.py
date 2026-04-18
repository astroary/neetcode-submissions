class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        cS = {} # tracking alphabet count

        # get count for letters in s
        for char in s:
            # u found a letter and increment its counter
            cS[char] = 1 + cS.get(char, 0)

        #subtract with letters from t
        for char in t:
            # means letter not there or t has more of that alphabet than s
            if char not in cS or cS[char] == 0:
                return False
            cS[char] -= 1

        return True
            
        