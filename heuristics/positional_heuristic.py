
def positional_heuristic(board):
    """
    Calculate score for player 1, then change the sign depending on player parameter
    """
    score = 0
    positional_score = board.config['scoring']['positional_score']
    piece_loc_tuples = board.get_piece_loc_tuples()
    for piece, x, y in piece_loc_tuples:
        d_score = piece.points
        d_score += (y if piece.player==1 else (board.config['board']['size']-y-1)) * positional_score
        score += d_score if piece.player == 1 else -d_score
    return score
