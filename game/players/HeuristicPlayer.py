
class HeuristicPlayer:

    def __init__(self, heuristic, args={}):
        self.heuristic = heuristic
        self.args = args

    def get_move(self, board):
        return self.get_best_move_for_next_player(board)

    def get_best_move_for_next_player(self, board):
        best_move = None

        if board.next_player == 1:
            max_score = -100000
            for move in board.get_moves_for_next_player():
                board.apply_move(move)

                score = self.heuristic(board, **self.args)
                if max_score < score:
                    best_move = move
                    max_score = score

                board.reverse_last_move()
        else:
            min_score = 100000
            for move in board.get_moves_for_next_player():
                board.apply_move(move)

                score = self.heuristic(board, **self.args)
                if min_score < score:
                    best_move = move
                    min_score = score

                board.reverse_last_move()

        return best_move