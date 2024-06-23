import random
from Game_logic import *

MINI, MAX = -1000, 1000


def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = [c for c in range(column_count) if is_valid_location(board, c)]

    if depth == 0 or check_win(board, 1) or check_win(board, 2) or len(valid_locations) == 0:
        if check_win(board, 2):
            return (None, 100000000000000)
        elif check_win(board, 1):
            return (None, -10000000000000)
        else:
            return (None, 0)

    if maximizingPlayer:
        value = MINI
        column = random.choice(valid_locations)
        for c in valid_locations:
            row = get_next_open_row(board, c)
            copy_board = np.copy(board)
            drop_piece(copy_board, row, c, 2)
            new_score = minimax(copy_board, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = c
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:
        value = MAX
        column = random.choice(valid_locations)
        for c in valid_locations:
            row = get_next_open_row(board, c)
            copy_board = np.copy(board)
            drop_piece(copy_board, row, c, 1)
            new_score = minimax(copy_board, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = c
            beta = min(beta, value)
            if beta <= alpha:
                break
        return column, value


