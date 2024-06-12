import pygame
import numpy as np
import sys
import math
from Game_logic import Create_board, Drop_piece, Valid_location, Check_win, Flipping_the_board, Next_open_row
from Desigh import make_board

pygame.init()

screen = pygame.display.set_mode(size=(800, 600))

board = Create_board()
game_over = False

SQUARESIZE = 100

make_board(board, screen)
pygame.display.update()

turn = 0

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
             # Vraag om input speler 1
            if turn == 0:
                posx = event.pos[0]
                column = int(math.floor(posx / SQUARESIZE))

                if Valid_location(board, column):
                    row = Next_open_row(board, column)
                    Drop_piece(board, row, column, 1)

                    if Check_win(board, 1):
                        print("Player 1 wins!")
                        game_over = True
            # # Vraag om input speler 2
            else:
                posx = event.pos[0]
                column = int(math.floor(posx / SQUARESIZE))

                if Valid_location(board, column):
                    row = Next_open_row(board, column)
                    Drop_piece(board, row, column, 2)

                    if Check_win(board, 2):
                        print("Player 2 wins!")
                        game_over = True

            Flipping_the_board(board)
            make_board(board, screen)

            turn += 1
            turn = turn % 2

