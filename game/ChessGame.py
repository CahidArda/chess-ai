from board import Board

class ChessGame:

    def __init__(self,
        players,
        ):
        self.board = Board()
        self.players = players

    def run_game(self, n_moves = 10):
        for i in range(n_moves):
            print(self.board)
            self.board.apply_move(self.players[0].get_move(self.board))
            self.board.apply_move(self.players[1].get_move(self.board))
        