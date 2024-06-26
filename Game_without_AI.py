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
    https://www.javatpoint.com/mini-max-algorithm-in-ai
    https://www.javatpoint.com/ai-alpha-beta-pruning
    """

    pygame.init()

    board, screen, draw_board = initialize_and_draw_board()

    game_over = False
    turn = random.randint(0, 1)

    my_font = pygame.font.SysFont("Aptos", 70)
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and turn == 0 and not game_over:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1 if turn == 0 else 2)

                    if check_win(board, 1 if turn == 0 else 2):
                        label = my_font.render(f"Player {turn + 1} wins!", 1, YELLOW)
                        screen.blit(label, (45, 15))
                        print(f"Player {turn + 1} wins!")
                        game_over = True

                    flipping_the_board(board)
                    draw_board(board, screen)

                    turn += 1
                    turn = turn % 2
        if game_over:
            pygame.time.wait(5000)
if __name__ == '__main__':
    Game_without_AI()