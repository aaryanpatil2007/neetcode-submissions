class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxArea = 0
        rows, cols = len(grid), len(grid[0])
        seen = set()

        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            currarea = 1
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while queue:
                r, c = queue.popleft()
                for direction in directions:
                    new_r = r + direction[0]
                    new_c = c + direction[1]
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1 and (new_r, new_c) not in seen:
                        seen.add((new_r, new_c))
                        queue.append((new_r, new_c))
                        currarea += 1
            if currarea > self.maxArea:
                self.maxArea = currarea

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    seen.add((r, c))
                    bfs(r, c)
        return self.maxArea
