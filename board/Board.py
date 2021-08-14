
class Board:

    def __init__(self, game):
        self.size = game.config['board']['size']
        self.tiles = [[None for i in range(self.size)] for j in range(self.size)]
        self.pieces = []

        game.fill_tiles(self)

    def add_piece(self, x, y, piece, mirror=False):
        self.pieces.append(piece)
        self.tiles[y][x] = piece

        if mirror:
            copy_piece = piece.copy()
            copy_piece.player = '0'
            self.tiles[self.size - y - 1][x] = copy_piece

    def get_tile(self, x, y):
        return self.tiles[y][x]

    def __str__(self):
        return "\n".join([" ".join(["--" if tile==None else str(tile) for tile in row]) for row in self.tiles])
