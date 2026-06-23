class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS , COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        def rotenFruit(r,c):
            nonlocal fresh
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                return 
            
            grid[r][c] = 2
            q.append((r,c))
            fresh -= 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()

                rotenFruit(r-1,c)
                rotenFruit(r+1,c)
                rotenFruit(r,c-1)
                rotenFruit(r,c+1)
            
            minutes += 1

        return minutes if fresh == 0 else -1



