class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+= str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = j = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            currLen = int(s[i:j])
            i = j+1
            j = i + currLen
            word = str(s[i:j])
            res.append(word)
            i = j
        return res