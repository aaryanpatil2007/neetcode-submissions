class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        self.currstring = ""
        rows = len(board)
        cols = len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        globset = set()


        def dfs(r, c):
            self.currstring += board[r][c]
            if self.currstring == word:
                return True
            if len(self.currstring) >= len(word):
                self.currstring = self.currstring[:-1]
                return False
            globset.add((r, c))
            for direction in directions:
                new_r = r + direction[0]
                new_c = c + direction[1]
                if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in globset:
                    if dfs(new_r, new_c):
                        return True
            self.currstring = self.currstring[:-1]
            globset.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c) == True:
                    return True
        return False
            


