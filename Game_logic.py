import numpy as np
import pygame
from Constants import *
import random

def create_board():
    """
    In deze functie wordt het bord aangemaakt.
    Dit is een lege martix met 6 rijen en 7 kolommen die met nullen zijn gevuld
    """
    board = np.zeros((row_count, column_count))
    return board


def drop_piece(board, row, column, piece):
    """
    In deze functie wordt er een steentje gevallen in de 6 bij 7 matrix met een 1 of 2
    """
    board[row][column] = piece

def is_valid_location(board, column):
    """
    Deze functie controleert of een steentje in de kolom kan worden geplaatst.
    Als dat niet kan krijg je een False terug en kan het niet.
    """
    return board[row_count - 1][column] == 0

def get_next_open_row(board, column):
    """
    Deze functie geeft de eerst beschikbare rij in een kolom aan waar een steentje kan plaatsen.
    Als dat niet kan krijg je een False terug en kan het niet en kan je het opnieuw proberen.
    """
    for r in range(row_count):
        if board[r][column] == 0:
            return r


def check_win(board, piece):
    """
    Controleert of er iemand heeft gewonnen.
    De functie doet dat in alle richtingen horizontaal, verticaal en diagonaal/.
    """
    for row in range(row_count):
        for column in range(column_count):
            if board[row][column] == piece:
                """Hier wordt gekeken of er horizontaal is gewonnen"""
                if column + 3 < column_count and all(board[row][column + i] == piece for i in range(4)):
                    return True
                """Hier wordt gekeken of er verticaal is gewonnen"""
                if row + 3 < row_count and all(board[row + i][column] == piece for i in range(4)):
                    return True
                """Hier wordt gekeken of de positive diagonaal heeft gewonnen"""
                if column + 3 < column_count and row + 3 < row_count and all(board[row + i][column + i] == piece for i in range(4)):
                    return True
                """Hier wordt gekeken of de negative diagonaal heeft gewonnen"""
                if column + 3 < column_count and row - 3 >= 0 and all(board[row - i][column + i] == piece for i in range(4)):
                    return True
    return False

def flipping_the_board(board):
    """
    Hier wordt het speelbord omgedraaid zodat de matrixen goed blijven staan.
    De reden hiervoor is dat speelbord mooi is en niet dat de steenjes boven aan verkeerd staan in je speelbord
    """
    print(np.flip(board, 0))

def initialize_and_draw_board():
    """
    Hier wordt het speel bord gemaakt zodat die er vizueel mooi uit ziet
    Dat komt door de hulp van PyGame
    """
    def draw_board(board, screen):
        """In dit stuk wordt blauwe vierkanten gemaakt en zwarte cirkles voor de lege plekken"""
        for c in range(column_count):
            for r in range(row_count):
                pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(screen, BLACK, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)
        """Hier worden de spelstukken van speler of ai gemaakt met de kleuren van rood en geel"""
        for c in range(column_count):
            for r in range(row_count):
                if board[r][c] == 1:
                    pygame.draw.circle(screen, RED, (
                        int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
                elif board[r][c] == 2:
                    pygame.draw.circle(screen, YELLOW, (
                        int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
        """Hier wordt elke keer als je een steentje is bijgegooid een hokje geel of rood geupdate"""
        pygame.display.update()
    """
    Hier wordt het de Pygame grote van het scherm opgegeven.
    Het bord wordt hier aangemaakt 
    """
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Connect Four")

    board = create_board()
    draw_board(board, screen)
    pygame.display.update()

    return board, screen, draw_board
