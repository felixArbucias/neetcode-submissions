class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])  
        visited = set()
        islands = 0 

        def dfs(r, c):
            # 1. are we out of bounds
            # 2. has this area in the grid been visited already
            # 3. if this area is not equal to an island (no need to traverse it)
            if (r < 0 or c < 0 or r >= ROW or c >= COL or (r,c) in visited or grid[r][c] == "0"): # out of bounds
                return # skip this iteration
            directions = [[0,1], [1,0], [0,-1], [-1, 0]]
            visited.add((r,c))
            for dr, dc in directions:
                dfs(r+dr,c+dc)

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and ((r,c)) not in visited:
                    dfs(r,c)
                    islands += 1 
        return islands 
                