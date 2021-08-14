
class Board:

    def __init__(self, game):
        self.size = game.size
        self.tiles = [[None for i in range(self.size)] for j in range(self.size)]
        self.pieces = []

        #game.fill_tiles(self)

    def add_piece(self, x, y, piece):
        self.pieces.append(piece)
        self.tiles[y][x] = piece

    def __str__(self):
        pass
