
def positional_heuristic(piece_loc_tuples, player, config):
    """
    Calculate score for player 1, then change the sign depending on player parameter
    """
    score = 0
    positional_score = config['scoring']['positional_score']
    for piece, x, y in piece_loc_tuples:
        d_score = piece.points
        d_score += (y if piece.player==1 else (config['board']['size']-y-1)) * positional_score
        score += d_score if piece.player == 1 else -d_score
    return score if player == 1 else -score 
