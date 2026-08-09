class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque()
        time = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]    

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
        while queue:      
            currlevel = len(queue)
            for i in range(currlevel):
                r, c = queue.popleft()
                for direction in directions:
                    new_r = r + direction[0]
                    new_c = c + direction[1]
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        queue.append((new_r, new_c))

            if queue:
                time += 1                

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return time