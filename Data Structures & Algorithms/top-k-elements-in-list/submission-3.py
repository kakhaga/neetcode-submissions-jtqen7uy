class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a max heap(-1), key being frequency
        # return top k(pop k times) and return the numbers

        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        heap = []
        
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
