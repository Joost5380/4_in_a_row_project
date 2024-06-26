import sys
import math
from Game_logic import *
from Constants import *
import random
from MINI_MAX_PRUNING import minimax
def MINIMAX_tegen_MINIMAX():
    pygame.init()

    board, screen, draw_board = initialize_and_draw_board()

    my_font = pygame.font.SysFont("Aptos", 70)
    turn = random.randint(0, 1)
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # AI turn
        if turn == 0 and not game_over:
            # Random AI
            col, minimax_score = minimax(board, 7, -1000, 1000, True)
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)
                if check_win(board, 1):
                    label = my_font.render("Random AI wins", 1, RED)
                    screen.blit(label, (45, 15))
                    print("MINIMAXXX AI wins!")
                    game_over = True

        elif turn == 1 and not game_over:
            # Minimax AI
            col, minimax_score = minimax(board, 5, -1000, 1000, True)
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)
                if check_win(board, 2):
                    label = my_font.render("Minimax AI wins", 1, YELLOW)
                    screen.blit(label, (45, 15))
                    print("Minimax AI wins!")
                    game_over = True

        flipping_the_board(board)
        draw_board(board, screen)

        turn = (turn + 1) % 2

    if game_over:
        pygame.time.wait(5000)

if __name__ == '__main__':
    MINIMAX_tegen_MINIMAX()