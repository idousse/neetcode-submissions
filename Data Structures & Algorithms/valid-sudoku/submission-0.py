class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(9):
            seen = set()
            for j in range(9):
                s = board[i][j]
                if s == ".":
                    continue
                if s in seen: 
                    return False
                seen.add(s)
        
        seen = set()
        for i in range(9):
            seen = set()
            for j in range(9):
                s = board[j][i]
                if s == ".":
                    continue
                if s in seen: 
                    return False
                seen.add(s)

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        s = board[box_row + i][box_col + j]
                        if s == ".":
                            continue
                        if s in seen:
                            return False
                        seen.add(s)
        return True
        