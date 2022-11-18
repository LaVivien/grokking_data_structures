# populate single digit number to matrix, find 3 adjacent cells have the same value
	
from random import randrange

#Time O(mxn), Space O(mxn)
def initialize_board(m, n):
    matrix = [[0 for j in range (n)] for i in range(m)]
    for  i in range (0, m):
        for j in range(0, n):
            matrix[i][j] = randrange(10)
    return matrix

#Time O(mxn), Space O(1)
def print_board(board):
    for i in range(0, len(board)) :
        s = ''
        for j in range (0, len(board[0])):    
            s += str(board[i][j]) + ' '
        print(s)

#Time O(mxn), Space O(1)
def checkBoard(board) :  
    rows = len(board)
    cols = len(board[0])

    for i in range(1,  rows-1):
        for j in range(1, cols-1):
            #left and right
            if board[i][j] == board[i][j-1] and board[i][j] == board[i][j+1]:
                return True

            #upper and below
            if board[i][j] == board[i-1][j] and board[i][j] == board[i+1][j] :
                return True

            #main Diagonal  
            if board[i][j] == board[i-1][j-1] and board[i][j] == board[i+1][j+1]:
                return True

            #Diagonal  
            if board[i][j] == board[i-1][j+1] and board[i][j] == board[i+1][j-1]:
                return True            
    return False
			
board = initialize_board(5,4)
print_board(board)
print(checkBoard(board))