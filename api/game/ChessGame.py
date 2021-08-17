from board import Board
import json

class ChessGame:

    def __init__(self, players):

        with open("config.json") as file:
            self.config = json.load(file)

        self.board = Board(self.config)
        self.players = players

    def run_game(self, n_moves = 10):
        print(self.board)
        for i in range(n_moves):
            self.board.apply_move(self.players[0].get_move(self.board))
            #print(self.board)
            self.board.apply_move(self.players[1].get_move(self.board))
            #print(self.board)

        with open(self.config['result']['save_moves_to'], 'w') as file:
            json.dump([str(m) for m in self.board.past_moves], file)