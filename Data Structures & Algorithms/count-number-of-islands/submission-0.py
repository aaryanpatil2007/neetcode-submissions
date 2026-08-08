class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            while queue:
                r, c = queue.popleft()
                for direction in directions:
                    new_r = r + direction[0]
                    new_c = c + direction[1]
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == "1" and (new_r, new_c) not in seen:
                        seen.add((new_r, new_c))
                        queue.append((new_r, new_c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and not (r, c) in seen:
                    bfs(r, c)
                    islands += 1
        return islands