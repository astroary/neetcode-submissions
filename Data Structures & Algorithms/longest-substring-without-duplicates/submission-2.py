class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        has = set()
        l = 0
        maxL = 0
        for r in range(len(s)):
            while s[r] in has:
                has.remove(s[l])
                l+=1
            has.add(s[r])
            maxL = max(maxL, r-l+1)
        return maxL