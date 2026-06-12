class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            horizontal = set()
            for j in board[i]:
                if j != "." and j not in horizontal:
                    horizontal.add(j)
                elif j in horizontal:
                    return False
        for i in range(9):
            vertical = set()
            for j in board:
                if j[i] != "." and j[i] not in vertical:
                    vertical.add(j[i])
                elif j[i] in vertical:
                    return False
        for z in range(0, 9, 3):
            for y in range (0, 9, 3):
                threebythree = set()
                for i in range(z, z+3, 1):
                    for j in range(y, y+3, 1):
                        if board[i][j] != "." and board[i][j] not in threebythree:
                            threebythree.add(board[i][j])
                        elif board[i][j] in threebythree:
                            return False
        return True
        

            

                
            
            
