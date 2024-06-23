import sys
import math
from Game_logic import *
from Constants import *

def Game_without_AI():

    """
    Bronnen 
    https://pygame.readthedocs.io/en/latest/1_intro/intro.html
    https://www.pygame.org/docs/ref/event.html#pygame.event.Event
    https://www.youtube.com/watch?v=y9VG3Pztok8
    https://www.youtube.com/watch?v=l-hh51ncgDI&t=585s 
    https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/
    """

    pygame.init()

    def draw_board(board):
        for c in range(column_count):
            for r in range(row_count):
                pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(screen, BLACK, (
                int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

        for c in range(column_count):
            for r in range(row_count):
                if board[r][c] == 1:
                    pygame.draw.circle(screen, RED, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
                elif board[r][c] == 2:
                    pygame.draw.circle(screen, YELLOW, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
        pygame.display.update()

    screen = pygame.display.set_mode(size)

    board = create_board()
    draw_board(board)
    pygame.display.update()
    game_over = False
    turn = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1 if turn == 0 else 2)

                    if check_win(board, 1 if turn == 0 else 2):
                        print(f"Player {turn + 1} wins!")
                        game_over = True

                    flipping_the_board(board)
                    draw_board(board)

                    turn += 1
                    turn = turn % 2