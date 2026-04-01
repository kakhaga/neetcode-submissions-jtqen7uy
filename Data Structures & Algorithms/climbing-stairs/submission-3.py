class Solution:
    def climbStairs(self, n: int) -> int:
        # 1,2,3,5
        
        if n < 3:
            return n
        
        l, r = 1,2
        for _ in range(2,n):
            l,r = r, l+r
        return r
        