class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}
        for i, n in enumerate(nums):
            # calc diff that i need to find in hashmap
            diff = target - n

            if diff in hashmap:
                # return index of first person, and index of current person
                return [hashmap[diff], i]

            # didnt find diff, so make a record in hashmap so can find this later
            hashmap[n] = i
        