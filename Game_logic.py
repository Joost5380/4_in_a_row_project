import numpy as np

row_count = 6
column_count = 7


def Create_board():
    board = np.zeros((row_count, column_count))
    return board

def Drop_piece(board, row, column, piece):
    board[row][column] = piece

def Valid_location(board, column):
    # De 5 zorgt ervoor dat je begint op de onderste rij
    return board[row_count-1][column] == 0

def Next_open_row(board, column):
    for ROW in range(row_count):
        if board[ROW][column] == 0:
            return ROW

def Flipping_the_board(board):
    print(np.flip(board, 0))

def Check_win(board, piece):
    for ROW in range(row_count):
        for COLUMN in range(column_count):
            if board[ROW][COLUMN] == piece:

                # Horizontale winst controleren
                if COLUMN + 3 < column_count and all(board[ROW][COLUMN + i] == piece for i in range(4)):
                    return True

                # Verticale winst controleren
                if ROW + 3 < row_count and all(board[ROW + i][COLUMN] == piece for i in range(4)):
                    return True

                # Positieve diagonale winst controleren
                if COLUMN + 3 < column_count and ROW + 3 < row_count and all(board[ROW + i][COLUMN + i] == piece for i in range(4)):
                    return True

                # Negatieve diagonale winst controleren
                if COLUMN + 3 < column_count and ROW - 3 >= 0 and all(board[ROW - i][COLUMN + i] == piece for i in range(4)):
                    return True
    return False
