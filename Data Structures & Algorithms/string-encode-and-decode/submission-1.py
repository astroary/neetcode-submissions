class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        
        return res

    def decode(self, s: str) -> List[str]:
        i = j = 0
        res = []

        while i < len(s):
            while s[j] != '#':
                j+=1
            currLen = int(s[i:j])
            i = j+1
            j = i + currLen
            currWord = s[i:j]
            res.append(currWord)
            i = j
        return res