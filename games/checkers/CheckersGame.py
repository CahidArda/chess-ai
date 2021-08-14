from board import Piece
from ..Game import Game

class CheckersGame(Game):
    
    def __init__(self):
        super().__init__("games\checkers\checkers.json")

    def fill_tiles(self, board, player = "1"):
        piece_config = self.config['pieceTypes']
        checker_piece_config = piece_config['checkerPiece']
        for column in range(board.size):
            board.add_piece(column, 1, Piece(
                checker_piece_config['pieceStr'],
                checker_piece_config['points'],
                player
            ), mirror = True)