class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        finallist = []

        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            seen = set()
            seen.add((r, c))
            pacific = False
            atlantic = False
            if r == 0 or c == 0:
                pacific = True
            if r == rows  - 1 or c == cols - 1:
                atlantic = True
            while queue:
                r, c = queue.popleft()
                currheight = heights[r][c]
                for direction in directions:
                    new_r, new_c = r + direction[0], c + direction[1]
                    if 0 <= new_r < rows and 0 <= new_c < cols and heights[new_r][new_c] <= currheight and (new_r, new_c) not in seen:
                        queue.append((new_r, new_c))
                        seen.add((new_r, new_c))
                        if new_c == 0 or new_r == 0:
                            pacific = True
                        if new_r == rows - 1 or new_c == cols - 1:
                            atlantic = True
            return pacific and atlantic
                        

        for r in range(rows):
            for c in range(cols):
                save = bfs(r, c)
                if save:
                    finallist.append([r, c])
                    
        return finallist