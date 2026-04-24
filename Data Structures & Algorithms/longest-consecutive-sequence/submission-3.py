class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        maxL = 0

        sn = set(nums)

        for num in sn:
            if (num-1) not in sn:
                currL = 1
                while(num+currL) in sn:
                    currL+=1
                maxL = max(maxL, currL)
        return maxL