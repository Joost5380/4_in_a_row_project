import sys
import math
from Game_logic import *
from Constants import *
from MINI_MAX_PRUNING import minimax

def Game_with_AI():
    pygame.init()
    """Hier wordt het spelbord gemaakt"""
    board, screen, draw_board = initialize_and_draw_board()

    my_font = pygame.font.SysFont("Aptos", 70)
    turn = random.randint(0, 1)  # Hier wordt bepaalt random wie er mag beginnen
    game_over = False  # Als het True is wordt het spel gesloten
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and turn == 0 and not game_over:
                # Hier wordt gekeken naar de x cordinaat van een muisklik om een steetje te plaatsen
                posx = event.pos[0]
                # Hiermee wordt bepaald de x cordinaat van de kolom
                col = int(math.floor(posx / SQUARESIZE))
                """
                Hier wordt gekenen of de locatie valide is.
                Verder wordt er gekeken of je een steentje op die plek mag zetten
                Als je hebt gewonnen komt dat in beeld en stopt het spel                       
                """
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
            """
            Minimax pruning AI
            Hier wordt een steentje neer gezet door de Minimax prunign algoritme
            Verder wordt er gekeken of je een steentje op die plek mag zetten
            Als dat zo is wordt er een steetje gezet
            Als je hebt gewonnen komt dat in beeld en stopt het spel
                        """
            col, minimax_score = minimax(board, 8, -1000, 1000, True)

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)

                if check_win(board, 2):
                    label = my_font.render("AI wins", 1, RED)
                    screen.blit(label, (45, 15))
                    print(f"Player {turn + 1} wins!")
                    game_over = True

                flipping_the_board(board)
                draw_board(board, screen)

                turn = (turn + 1) % 2  # Hier wordt gezord dat je van speler wisselt
                # Als het spel is afgelopen blijft het even staan
        if game_over:
            pygame.time.wait(5000)

if __name__ == '__main__':
    Game_with_AI()
