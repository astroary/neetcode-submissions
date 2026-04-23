class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  #mapping charCount to list of groupAnagrams

        for s in strs:
            count = [0] * 26 # a ... z
            for char in s:
                # map 'a' to 0 and 'z' to 25 using ASCII vals
                count[ord(char)-ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())