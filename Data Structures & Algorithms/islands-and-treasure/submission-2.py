class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()


        def addLand(r,c,dist):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 2147483647:
                return

            grid[r][c] = dist
            q.append((r,c))



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))

        dist = 1
        while q:
            for _ in range(len(q)):
                r , c = q.popleft()

                addLand(r-1,c,dist)
                addLand(r+1,c,dist)
                addLand(r,c-1,dist)
                addLand(r,c+1,dist)

            dist += 1

