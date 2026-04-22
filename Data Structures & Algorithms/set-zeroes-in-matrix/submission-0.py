class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        columns = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows.add(r)
                    columns.add(c)
    
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in rows or c in columns:
                    matrix[r][c] = 0
        