from .Piece import Piece
from .Move import Move
import json

class Board:

    def __init__(self):
        
        with open("config.json") as file:
            self.config = json.load(file)
        self.score_d = {piece["piece_str"]:piece["points"] for piece in self.config['pieces'].values()}
        
        self.size = self.config['board']['size']
        self.tiles = [[None for i in range(self.size)] for j in range(self.size)]
        self.pieces = []
        self.past_moves = []
        self.next_player = 0

        self.piece_loc_tuples_updated = False

        self.__fill_board()

    # ---------------
    # Get Moves
    # ---------------

    def get_piece_loc_tuples(self, player = None):
        if not self.piece_loc_tuples_updated:
            self.__update_piece_loc_tuples()
        
        if player == None:
            all_tuples = []
            all_tuples.extend(self.piece_loc_tuples[0])
            all_tuples.extend(self.piece_loc_tuples[1])
            return all_tuples
        else:
            return self.piece_loc_tuples[player]        


    def __update_piece_loc_tuples(self):
        if self.piece_loc_tuples_updated:
            return
        self.piece_loc_tuples_updated = True

        self.piece_loc_tuples = [[], []]
        for y in range(self.size):
            for x in range(self.size):
                tile = self.__get_tile(x, y)
                if tile != None:
                    self.piece_loc_tuples[tile.player].append((tile, x, y))
        

    def __get_piece_loc_tuples_for_next_player(self):
        return self.get_piece_loc_tuples(self.next_player)

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
                    if y==(1 if self.next_player == 1 else self.size-2) and self.__tile_on_board(x, y2) and self.__tile_is_empty(x, y2):
                        moves.append(Move(x, y, x, y2))

            # checking king
            if piece.piece_str == pieces_config['king']['piece_str']:
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx==0 and dy==0:
                            pass
                        x2 = x + dx
                        y2 = y + dy
                        if self.__tile_on_board(x2, y2) and not self.__allied_piece_in_tile(x2, y2):
                            moves.append(Move(x, y, x2, y2))

            if piece.piece_str == pieces_config['knight']['piece_str']:
                for dx, dy in [(2,1), (1,2)]:
                    for x_sign, y_sign in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                        x2 = x + x_sign * dx
                        y2 = y + y_sign * dy
                        if self.__tile_on_board(x2, y2) and not self.__allied_piece_in_tile(x2, y2):
                            moves.append(Move(x, y, x2, y2))


        return moves

    # ---------------
    # Apply Moves
    # ---------------

    def apply_move(self, move):
        self.past_moves.append(move)
        self.piece_loc_tuples_updated = False

        move.removed_piece = self.tiles[move.y2][move.x2]
        self.tiles[move.y2][move.x2] = self.tiles[move.y1][move.x1]
        self.tiles[move.y1][move.x1] = None
        self.next_player = 1 - self.next_player

    def reverse_last_move(self):
        move = self.past_moves.pop()
        self.piece_loc_tuples_updated = False

        self.tiles[move.y1][move.x1] = self.tiles[move.y2][move.x2]
        self.tiles[move.y2][move.x2] = move.removed_piece
        self.next_player = 1 - self.next_player

    # ---------------
    # Private Methods
    # ---------------

    def __opponent_piece_in_tile(self, x, y):
        tile = self.__get_tile(x, y)
        return tile != None and self.next_player != tile.player

    def __allied_piece_in_tile(self, x, y):
        tile = self.__get_tile(x, y)
        return tile != None and self.next_player == tile.player


    def __get_tile(self, x, y):
        return self.tiles[y][x]
    
    def __tile_is_empty(self, x, y):
        return self.__get_tile(x, y) == None

    def __fill_board(self):
        pieces_config = self.config['pieces']
        for piece_config in pieces_config.values():

            positions_config = piece_config['positions']
            for column in positions_config['columns']:
                self.__add_piece(
                    column,
                    positions_config['row'],
                    Piece(
                        piece_config['piece_str'],
                        piece_config['points'],
                        1
                    ),
                    mirror = True
                )

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