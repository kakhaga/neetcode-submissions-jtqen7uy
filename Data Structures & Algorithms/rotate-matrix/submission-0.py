class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # reverse the row order
        for row_num in range(n//2):
            matrix[row_num], matrix[n-row_num-1] = matrix[n-row_num-1],matrix[row_num]
        print(matrix)
        # transpose the matrix
        # 00,01,02,03
        # 10,11,12,13
        # 20,21,22,23
        # 30,31,32,33
        # swap positions at i,j -> n-i-1, m-j-1
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 
    
        print(matrix)