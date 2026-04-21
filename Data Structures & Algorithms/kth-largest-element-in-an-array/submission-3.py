class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # nums.sort()
        # return nums[(len(nums))-k]
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0]

        # return heapq.nlargest(k, nums)[-1]
        