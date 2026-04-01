class Solution:
    def rob(self, nums: List[int]) -> int:
        # 2, 9, 8, 3, 6
        # 2,9, 10, 12, 16
        rob1, rob2 = 0, 0

        for num in nums:
            rob1, rob2 = rob2, max(rob2, num + rob1)
        
        return rob2




