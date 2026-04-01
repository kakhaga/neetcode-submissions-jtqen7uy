class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCtr = {}
        
        # create a map of all elements
        # with thier frequency
        for i in nums:
            freqCtr[i] = freqCtr.get(i,0) + 1
        
        heap = []

        for num in freqCtr.keys():
            heapq.heappush(heap, (freqCtr[num], num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res