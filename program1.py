class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    
        
        def test(a, c):
            if a < 0 or a >= len(grid) or c < 0 or c >= len(grid[0]) or grid[a][c] == 'W':
                return
            grid[a][c] = 'W'  
            test(a + 1, c)
            test(a - 1, c)
            test(a, c + 1)
            test(a, c - 1)
        
        num_islands = 0
        for a in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[a][c] == 'L':
                    num_islands += 1
                    test(a, c)
        
        return num_islands
