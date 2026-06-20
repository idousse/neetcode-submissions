class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        
        # 1. (DFS) capture all the cells that can go to pacific ocean and capture all the cells that can go to atlantic ocean in SETS
        # capture: should compare all around cells, if value is larger, add it 
        # 2 . Join those sets (a & b)

        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()


        def dfs(r,c,visited, prevHeight):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                (r,c) in visited 
                or heights[r][c] < prevHeight):
                return
            
            visited.add((r,c))
            dfs(r+1,c,visited, heights[r][c])
            dfs(r-1,c,visited, heights[r][c])
            dfs(r,c-1,visited, heights[r][c])
            dfs(r,c+1,visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS-1, c,atlantic, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS-1,atlantic, heights[r][COLS-1])

        return [list(cell) for cell in pacific & atlantic]