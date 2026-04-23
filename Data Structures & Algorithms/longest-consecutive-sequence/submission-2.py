class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxL = 0

        for n in nums:
            if n-1 not in numSet:
                currL = 1
                while (n+currL) in numSet:
                    currL +=1
                maxL = max(maxL, currL)
        return maxL
