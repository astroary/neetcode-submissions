class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # nums.sort()
        # return nums[(len(nums))-k]


        # minHeap = []
        # for num in nums:
        #     heapq.heappush(minHeap, num)
        #     if len(minHeap) > k:
        #         heapq.heappop(minHeap)
        # return minHeap[0]
        
        
        h = []
        for n in nums:
            heapq.heappush(h,n)
            if len(h) > k:
                heapq.heappop(h)
        return h[0]