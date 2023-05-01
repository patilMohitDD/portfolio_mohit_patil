from random import randint
from constants import sudokus


def solver(board):
    n = 9
    def isValid(row, col, ch, board):
        row, col = int(row), int(col)
        
        for i in range(9):
            
            if board[i][col] == ch:
                return False
            if board[row][i] == ch:
                return False
            
            if board[3*(row//3) + i//3][3*(col//3) + i%3] == ch:
                return False
        
        return True
        
    def backtracking(row, col, board):
        if row == n:
            return True
        if col == n:
            return backtracking(row+1, 0, board)
        
        if board[row][col] == ".":
            for i in range(1, 10):
                if isValid(row, col, str(i), board):
                    board[row][col] = str(i)
                    
                    if backtracking(row, col + 1, board):
                        return True
                    else:
                        board[row][col] = "."
            return False
        else:
            return backtracking(row, col + 1, board)
        
    backtracking(0, 0, board)
    return board

def generate_id():
    while True:
        id = randint(1, 100)
        if id not in db.keys():
            return str(id)
