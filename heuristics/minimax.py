from heuristics.positional_heuristic import positional_heuristic

def minimax(board, depth=3, alpha = -100000, beta = 100000):
    """
    Apply minimax with alpha-beta pruning to evaluate a board position
    """

    if depth == 0: # haven't added end game conditions yet
        piece_loc_tuples = board.get_piece_loc_tuples()
        return positional_heuristic(board)
    
    # player 1 is maximizing
    if board.next_player == 1:
        maxEval = -100000
        for move in board.get_moves_for_next_player():
            board.apply_move(move)            

            curEval = minimax(board, depth-1, alpha, beta)
            maxEval = max(maxEval, curEval)
            alpha   = max(alpha, curEval)
            board.reverse_last_move()
            if beta <= alpha:
                break 
        return maxEval
    else:
        minEval = 100000
        for move in board.get_moves_for_next_player():
            board.apply_move(move)
            
            curEval = minimax(board, depth-1, alpha, beta)
            minEval = min(minEval, curEval)
            beta    = min(beta, curEval)
            board.reverse_last_move()
            if beta <= alpha:
                break
        return minEval