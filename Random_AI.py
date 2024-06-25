import sys
import math
from Game_logic import *
from Constants import *
from MINI_MAX_PRUNING import minimax

def Game_with_AI():
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
    pygame.display.set_caption("Connect Four")

    board = create_board()
    draw_board(board)
    pygame.display.update()
    my_font = pygame.font.SysFont("Aptos", 70)
    turn = 0
    game_over = False
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
                        label = my_font.render("Player wins", 1, RED)
                        screen.blit(label, (45, 15))
                        print(f"Player {turn + 1} wins!")
                        game_over = True

                    flipping_the_board(board)
                    draw_board(board)

                    turn += 1
                    turn = turn % 2

        if turn == 1 and not game_over:
            col =
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)

                if check_win(board, 2):
                    label = my_font.render("AI wins", 1, RED)
                    screen.blit(label, (45, 15))
                    print(f"Player {turn + 1} wins!")
                    game_over = True

                flipping_the_board(board)
                draw_board(board)

                turn += 1
                turn = turn % 2

        if game_over:
            pygame.time.wait(5000)

