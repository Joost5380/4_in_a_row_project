import random
from Game_logic import *
import numpy as np
from Constants import *
# Dit is de pseudo code die ik heb gebruikt
## https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning

def minimax(board, depth, alpha, beta, maximizingPlayer):
    """
    Hier is het minimax algoritme met alpha beta pruning
    """
    # Bepaalt de geldige loctaties
    valid_locations = [c for c in range(column_count) if is_valid_location(board, c)]
    # Bekijkt of je gewonnen of verloren hebt
    if depth == 0 or check_win(board, 1) or check_win(board, 2) or len(valid_locations) == 0:
        # Hier is de computer de winner
        if check_win(board, 2):
            return (None, 100000000000000)
        # Hier is de tegenstander de winner
        elif check_win(board, 1):
            return (None, -10000000000000)
        # Een gelijkst spel
        else:
            return (None, Looking_at_board_positions(board, 2))

    if maximizingPlayer:
        value = MINI
        # Hier wordt eerst een willekeurige zet gedaan
        column = random.choice(valid_locations)
        for c in valid_locations:
            row = get_next_open_row(board, c)
            copy_board = np.copy(board)
            drop_piece(copy_board, row, c, 2)
            # Het wordt recursive over heen gegaan om een score te krijgen
            new_score = minimax(copy_board, depth - 1, alpha, beta, False)[1]
            # Hier wordt gekeken over een bepaalde scoren beter is als dat zo is krijg je een nieuwe waarde
            if new_score > value:
                value = new_score
                column = c
            # Hier wordt alpha geupdate
            alpha = max(alpha, value)
            # Als er geen beter score kan komen wordt die opgezegt dat is het pruning gedeelte
            if alpha >= beta:
                break
        return column, value
    else:
        value = MAX
        # Hier wordt eerst een willekeurige zet gedaan
        column = random.choice(valid_locations)
        for c in valid_locations:
            row = get_next_open_row(board, c)
            copy_board = np.copy(board)
            drop_piece(copy_board, row, c, 1)
            # Het wordt recursive over heen gegaan om een score te krijgen
            new_score = minimax(copy_board, depth - 1, alpha, beta, True)[1]
            # Hier wordt gekeken over een bepaalde scoren beter is als dat zo is krijg je een nieuwe waarde
            if new_score < value:
                value = new_score
                column = c
            # Hier wordt beta geupdate
            beta = min(beta, value)
            # Hier wordt gekeken over een bepaalde scoren beter is als dat zo is krijg je een nieuwe waarde
            if beta <= alpha:
                break
        return column, value

def minimax_without_pruning(board, depth, maximizingPlayer):
    """
    Hier is het minimax algoritme zonder alpha beta pruning.
    """
    valid_locations = [c for c in range(column_count) if is_valid_location(board, c)]
    if depth == 0 or check_win(board, 1) or check_win(board, 2) or len(valid_locations) == 0:
        if check_win(board, 2):
            return (None, 100000000000000)
        elif check_win(board, 1):
            return (None, -10000000000000)
        else:
            return (None, Looking_at_board_positions(board, 2))

    if maximizingPlayer:
        value = MINI
        column = random.choice(valid_locations)
        for c in valid_locations:
            row = get_next_open_row(board, c)
            copy_board = np.copy(board)
            drop_piece(copy_board, row, c, 2)
            new_score = minimax_without_pruning(copy_board, depth - 1, False)[1]
            if new_score > value:
                value = new_score
                column = c
        return column, value
    else:
        value = MAX
        column = random.choice(valid_locations)
        for c in valid_locations:
            row = get_next_open_row(board, c)
            copy_board = np.copy(board)
            drop_piece(copy_board, row, c, 1)
            new_score = minimax_without_pruning(copy_board, depth - 1, True)[1]
            if new_score < value:
                value = new_score
                column = c
        return column, value

def Looking_at_board_positions(board, piece):
    score = 0
    opp_piece = 1 if piece == 2 else 2

    """Pioriteit om stenen in het midden te gooien zodat de AI beter wordt"""
    column_center_board = [int(i) for i in list(board[:, column_count // 2])]
    count_center_board = column_center_board.count(piece)
    score += count_center_board * 2

    """Hiermee worden de scoring bijgehouden met de horizontale steentjes"""
    for r in range(row_count):
        for c in range(column_count - 3):
            window = board[r, c:c + 4]
            window += score_window(window, piece, opp_piece)

    """Hiermee worden de scoring bijgehouden met de verticale steentjes"""
    for c in range(column_count):
        for r in range(row_count - 3):
            window = board[r:r + 4, c]
            score += score_window(window, piece, opp_piece)

    """Hiermee worden de scoring bijgehouden met de diagonaal de positive helling"""
    for r in range(row_count - 3):
        for c in range(column_count - 3):
            window = [board[r + i, c + i] for i in range(4)]
            score += score_window(window, piece, opp_piece)


    """Hiermee worden de scoring bijgehouden met de diagonaal de negative helling"""
    for r in range(3, row_count):
        for c in range(column_count - 3):
            window = [board[r - i, c + i] for i in range(4)]
            score += score_window(window, piece, opp_piece)
    return score

def score_window(window, piece, opp_piece):
    """Hier worden de scores berekent en waar je punten voor geeft"""
    window = list(window)
    score = 0

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(0) == 1:
        score -= 4.3
    elif window.count(opp_piece) == 2 and window.count(0) == 2:
        score -= 2

    return score
