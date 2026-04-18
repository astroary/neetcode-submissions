class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has = set()
        for i in range(len(nums)):
            if nums[i] in has:
                return True
            has.add(nums[i])
        return False
        