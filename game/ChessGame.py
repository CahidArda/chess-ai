from board import Board

class ChessGame:

    def __init__(self,
        players,
        ):
        self.board = Board()
        self.players = players

    def run_game(self, n_moves = 10):
        print(self.board)
        for i in range(n_moves):
            self.board.apply_move(self.players[0].get_move(self.board))
            print(self.board)
            self.board.apply_move(self.players[1].get_move(self.board))
            print(self.board)