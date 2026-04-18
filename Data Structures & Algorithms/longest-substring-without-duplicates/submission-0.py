class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxl = 0, 0
        has = set()

        for r in range(len(s)):
            while s[r] in has:
                has.remove(s[l])
                l +=1
            has.add(s[r])
            maxl = max(maxl, r-l+1)
        return maxl
        
        