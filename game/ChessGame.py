from board import Board

class ChessGame:

    def __init__(self,
        player_color,
        players,
        ):
        self.board = Board()
        self.board.next_player = 1 if player_color == 'black' else 0
        self.players = players

    def run_game(self, n_moves = 10):
        for i in range(n_moves):
            self.board.apply_move(self.players[0].get_move(self.board))
            self.board.apply_move(self.players[1].get_move(self.board))
        