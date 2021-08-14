from .Piece import Piece
import json

class Board:

    def __init__(self):
        with open("config.json") as file:
            self.config = json.load(file)
        self.size = self.config['board']['size']
        self.tiles = [[None for i in range(self.size)] for j in range(self.size)]
        self.pieces = []

        self.fill_board()

    def add_piece(self, x, y, piece, mirror=False):
        self.pieces.append(piece)
        self.tiles[y][x] = piece

        if mirror:
            copy_piece = piece.copy()
            copy_piece.player = '0'
            self.tiles[self.size - y - 1][x] = copy_piece

    def get_tile(self, x, y):
        return self.tiles[y][x]

    def fill_board(self):
        pieces_config = self.config['pieces']
        for column in range(self.size):

            # adding pawns
            pawn_config = pieces_config['pawn']
            self.add_piece(
                column, 1,
                Piece(
                    pawn_config['piece_str'],
                    pawn_config['points'],
                    "1"),
                mirror = True)

    def get_piece_loc_tuples(self):
        tuples = []
        for y in range(self.size):
            for x in range(self.size):
                tile = self.get_tile(x, y)
                if tile != None:
                    tuples.append((tile, x, y))
        return tuples

    def get_all_possible_moves(self):
        piece_loc_tuples = self.get_piece_loc_tuples()
        for piece, x, y in piece_loc_tuples:
            print(piece, x, y)

    def __str__(self):
        string = "    %s\n" % "  ".join([str(i) for i in range(self.size)])
        for y in range(self.size):
            string += "%d:  %s\n" % (y, " ".join(["--" if tile==None else str(tile) for tile in self.tiles[y]]))
        return string