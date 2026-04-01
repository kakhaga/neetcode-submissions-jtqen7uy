class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])
        dp = {}
        def dfs(r,c,prevVal):
            # base conditions
            if r >= ROW or r < 0 or c >= COL or c < 0 or matrix[r][c] <= prevVal:
                return 0
            
            if (r,c) in dp:
                return dp[(r,c)]
            res = 1
            
            res = max(res, 1 + dfs(r+1,c,matrix[r][c]))
            res = max(res, 1 + dfs(r,c+1,matrix[r][c]))
            res = max(res, 1 + dfs(r-1,c,matrix[r][c]))
            res = max(res, 1 + dfs(r,c-1,matrix[r][c]))
            dp[(r,c)] = res
            return res

        for i in range(ROW):
            for j in range(COL):
                dfs(i,j,-1)
        return max(dp.values())
            