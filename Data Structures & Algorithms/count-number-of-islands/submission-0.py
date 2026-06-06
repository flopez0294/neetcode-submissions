class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0, -1]]
        R, C = len(grid), len(grid[0])
        num = 0

        def dfs(r,c):
            if r < 0 or c < 0 or  r >= R or c >= C or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    dfs(r,c)
                    num += 1
        return num