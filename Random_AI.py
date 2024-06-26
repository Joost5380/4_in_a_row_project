import sys
import math
from Game_logic import *
from Constants import *
import random
def Random_AI_AI():
    pygame.init()

    board, screen, draw_board = initialize_and_draw_board()
    my_font = pygame.font.SysFont("Aptos", 70)

    turn = random.randint(0, 1)

    game_over = False
    while not game_over:
        for event in pygame.event.get() and turn == 0 and not game_over:
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
                    draw_board(board, screen)

                    turn += 1
                    turn = turn % 2

        if turn == 1 and not game_over:
            col = random.randint(0, column_count - 1)

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)

                if check_win(board, 2):
                    label = my_font.render("AI wins", 1, YELLOW)
                    screen.blit(label, (45, 15))
                    print("AI wins!")
                    game_over = True

                flipping_the_board(board)
                draw_board(board, screen)

                turn = (turn + 1) % 2


        if game_over:
            pygame.time.wait(5000)

if __name__ == '__main__':
    Random_AI_AI()