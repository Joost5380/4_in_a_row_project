import numpy as np
import pygame
from Constants import *

# In deze functie wordt het bord aangemaakt
def create_board():
    board = np.zeros((row_count, column_count))
    return board

# In deze functie wordt gekeken of je een stukje kan plaatsen
def drop_piece(board, row, column, piece):
    board[row][column] = piece

# Deze functie controleert of een piece in de kolom kan worden geplaatst.
def is_valid_location(board, column):
    return board[row_count - 1][column] == 0

# Deze functie geeft de eerst beschikbare rij in een kolom.
def get_next_open_row(board, column):
    for r in range(row_count):
        if board[r][column] == 0:
            return r

# Deze functie kijkt of iemand heeft gewonnen.
def check_win(board, piece):
    for row in range(row_count):
        for column in range(column_count):
            if board[row][column] == piece:
                # Hier wordt gekeken of er horizontaal is gewonnen
                if column + 3 < column_count and all(board[row][column + i] == piece for i in range(4)):
                    return True
                # Hier wordt gekeken of er verticaal is gewonnen
                if row + 3 < row_count and all(board[row + i][column] == piece for i in range(4)):
                    return True
                # Hier wordt gekeken of de positive diagonaal heeft gewonnen
                if column + 3 < column_count and row + 3 < row_count and all(board[row + i][column + i] == piece for i in range(4)):
                    return True
                # Hier wordt gekeken of de negative diagonaal heeft gewonnen
                if column + 3 < column_count and row - 3 >= 0 and all(board[row - i][column + i] == piece for i in range(4)):
                    return True
    return False

# Dit is om te kijken of het goed werkt en om te zorgen dat de index niet boven aan begint
def flipping_the_board(board):
    print(np.flip(board, 0))