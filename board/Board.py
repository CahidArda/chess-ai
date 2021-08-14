from .Piece import Piece
from .Move import Move
import json

class Board:

    def __init__(self):
        with open("config.json") as file:
            self.config = json.load(file)
        self.size = self.config['board']['size']
        self.tiles = [[None for i in range(self.size)] for j in range(self.size)]
        self.pieces = []
        self.past_moves = []
        self.next_player = 0

        self.__fill_board()

    def __get_piece_loc_tuples_for_next_player(self):
        tuples = []
        for y in range(self.size):
            for x in range(self.size):
                tile = self.__get_tile(x, y)
                if tile != None and tile.player == self.next_player:
                    tuples.append((tile, x, y))
        return tuples

    def get_moves_for_next_player(self):
        moves = []

        piece_loc_tuples = self.__get_piece_loc_tuples_for_next_player()
        pieces_config = self.config['pieces']
        for piece, x, y in piece_loc_tuples:
            
            # checking pawns
            if piece.piece_str == pieces_config['pawn']['piece_str']:
                # diagonals
                y_direction = 1 if self.next_player==1 else -1
                for dx in [-1, 1]:
                    x2 = x + dx
                    y2 = y + y_direction

                    if self.__tile_on_board(x2, y2) and self.__opponent_piece_in_tile(x2, y2):
                        moves.append(Move(x, y, x2, y2))
                
                # straight
                y2 = y+y_direction
                if self.__tile_on_board(x, y2) and self.__tile_is_empty(x, y2):
                    moves.append(Move(x, y, x, y2))
                    y2 += y_direction
                    if not piece.moved_before and self.__tile_on_board(x, y2) and self.__tile_is_empty(x, y2):
                        moves.append(Move(x, y, x, y2))

        return moves

    def apply_move(self, move):
        self.past_moves.append(move)
        move.removed_piece = self.tiles[move.y2][move.x2]
        self.tiles[move.y2][move.x2] = self.tiles[move.y1][move.x1]
        self.tiles[move.y1][move.x1] = None
        self.next_player = 1 - self.next_player

    def reverse_last_move(self):
        move = self.past_moves.pop()
        self.tiles[move.y1][move.x1] = self.tiles[move.y2][move.x2]
        self.tiles[move.y2][move.x2] = move.removed_piece
        self.next_player = 1 - self.next_player

    """
    def __alied_piece_in_tile(self, x, y):
        tile = __get_tile(x, y)
        return tile != None and self.next_player == tile.player
    """

    def __opponent_piece_in_tile(self, x, y):
        tile = self.__get_tile(x, y)
        return tile != None and self.next_player != tile.player

    def __get_tile(self, x, y):
        return self.tiles[y][x]
    
    def __tile_is_empty(self, x, y):
        return self.__get_tile(x, y) == None

    def __fill_board(self):
        pieces_config = self.config['pieces']
        for column in range(self.size):

            # adding pawns
            pawn_config = pieces_config['pawn']
            self.__add_piece(
                column, 1,
                Piece(
                    pawn_config['piece_str'],
                    pawn_config['points'],
                    1),
                mirror = True)

    def __add_piece(self, x, y, piece, mirror=False):
        self.pieces.append(piece)
        self.tiles[y][x] = piece

        if mirror:
            copy_piece = piece.copy()
            copy_piece.player = 0
            self.tiles[self.size - y - 1][x] = copy_piece

    def __tile_on_board(self, x, y):
        if x < 0 or self.size <= x:
            return False
        if y < 0 or self.size <= y:
            return False
        return True   

    def __str__(self):
        string = "    %s\n" % "  ".join([str(i) for i in range(self.size)])
        for y in range(self.size):
            string += "%d:  %s\n" % (y, " ".join(["--" if tile==None else str(tile) for tile in self.tiles[y]]))
        return string