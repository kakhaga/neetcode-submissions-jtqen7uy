class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first = 1
        second = 2

        for i in range(2,n):
            first, second = second, first+second
        
        return second
