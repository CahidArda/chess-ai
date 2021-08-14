from ..Game import Game

class CheckersGame(Game):
    
    def __init__(self):
        super().__init__("games\checkers\checkers.json")

    def fill_tiles(self, board, player = "1"):
        for column in range(board.size):
            board.add_piece(column, 1, Piece(
                
            ))