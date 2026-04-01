class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DP -> store the number of ways you can reach 
        # [i][j] column by adding values from [i-1][j] & [i][j-1]
        # improvement
        # only need the previous row
        # keep updating this row from left to right
        # keep left most value as zero
        arr = [1] * (n + 1)
        arr[0] = 0

        for i in range(m-1):
            for j in range(1,n+1):
                arr[j] = arr[j] + arr[j-1]
        return arr[-1]

        