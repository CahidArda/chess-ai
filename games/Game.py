
from board import Piece

import json

class Game:
    
    def __init__(self, configPath):
        with open(configPath) as file:
            self.config = json.load(file)

    def _add_opponent_pieces(self, player = "0"):
        opponent_pieces = []
        for piece in self.pieces:
            opponent_pieces.append(Piece(
                piece.x,
                self.size - piece.y - 1,
                piece.pieceStr, 
                piece.points,
                player
            ))
        self.pieces.extend(opponent_pieces)