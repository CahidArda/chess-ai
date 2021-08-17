from .Piece import Piece
from .Move import Move


class Board:

    def __init__(self, config):
        
        self.config = config

        self.score_d = {piece["piece_str"]:piece["points"] for piece in self.config['pieces'].values()}
        self.size = self.config['board']['size']
        self.tiles = [[None for i in range(self.size)] for j in range(self.size)]
        self.pieces = [[], []]
        self.past_moves = []
        self.next_player = 0

        self.__fill_board()

    # ---------------
    # Get Moves
    # ---------------

    def validate_positions(self):
        for x in range(self.size):
            for y in range(self.size):
                tile = self.__get_tile(x, y)
                if tile != None:
                    assert (tile.x == x and tile.y == y), "piece loc is not valid: %d, %d, %d, %d" % (tile.x, tile.y, x, y)

    def get_piece_loc_tuples(self, player = None):
        pieces = self.__get_pieces(player)
        return [(piece, piece.x, piece.y) for piece in pieces]

    def __get_pieces(self, player = None):
        if player == None:
            all_pieces = []
            all_pieces.extend(self.pieces[0])
            all_pieces.extend(self.pieces[1])
            return all_pieces
        else:
            return self.pieces[player]

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

            # checking rook
            if piece.piece_str == pieces_config['rook']['piece_str']:
                moves.extend(self.__search_perpendicular_moves(x,y))

            # checking knight
            if piece.piece_str == pieces_config['knight']['piece_str']:
                for dx, dy in [(2,1), (1,2)]:
                    for x_sign, y_sign in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                        x2 = x + x_sign * dx
                        y2 = y + y_sign * dy
                        if self.__tile_on_board(x2, y2) and not self.__allied_piece_in_tile(x2, y2):
                            moves.append(Move(x, y, x2, y2))

            # checking bishop
            if piece.piece_str == pieces_config['bishop']['piece_str']:
                moves.extend(self.__search_diagonal_moves(x,y))

            # checking queen
            if piece.piece_str == pieces_config['queen']['piece_str']:
                moves.extend(self.__search_perpendicular_moves(x,y))
                moves.extend(self.__search_diagonal_moves(x,y))


        return moves

    def __search_perpendicular_moves(self, x, y):
        return self.__search_offset_recursively(x,y, [(1,0), (0,1), (-1,0), (0,-1)])

    def __search_diagonal_moves(self, x, y):
        return self.__search_offset_recursively(x,y, [(1,1), (1,-1), (-1,1), (-1,-1)])

    def __search_offset_recursively(self, x, y, offsets):
        moves = []
        for dx, dy in offsets:
            x2 = x + dx
            y2 = y + dy
            while self.__tile_on_board(x2, y2):

                if self.__opponent_piece_in_tile(x2, y2):
                    moves.append(Move(x, y, x2, y2))
                    break
                elif self.__allied_piece_in_tile(x2, y2):
                    break

                moves.append(Move(x, y, x2, y2))

                x2 += dx
                y2 += dy

        return moves


    # ---------------
    # Apply Moves
    # ---------------

    def apply_move(self, move):
        self.past_moves.append(move)

        if self.__opponent_piece_in_tile(move.x2, move.y2):
            move.removed_piece = self.tiles[move.y2][move.x2]
            self.__remove_piece(move.x2, move.y2)

        self.tiles[move.y1][move.x1].move_to(move.x2, move.y2)

        self.tiles[move.y2][move.x2] = self.tiles[move.y1][move.x1]
        self.tiles[move.y1][move.x1] = None

        self.next_player = 1 - self.next_player

    def reverse_last_move(self):
        move = self.past_moves.pop()

        self.tiles[move.y2][move.x2].move_to(move.x1, move.y1)

        self.tiles[move.y1][move.x1] = self.tiles[move.y2][move.x2]
        self.tiles[move.y2][move.x2] = move.removed_piece
        
        if move.removed_piece != None:
            self.__add_piece(move.removed_piece)

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
                
                piece = Piece(piece_config['piece_str'],
                    piece_config['points'],
                    1,
                    column,
                    positions_config['row']
                )

                self.__add_piece(piece, mirror = True)

    def __add_piece(self, piece, mirror=False):
        self.pieces[piece.player].append(piece)
        self.tiles[piece.y][piece.x] = piece

        if mirror:
            copy_piece = piece.mirrored_copy(self.size)
            self.__add_piece(copy_piece)

    def __remove_piece(self, x, y):
        assert not self.__tile_is_empty(x, y), "Can not remove piece: Tile is empty."
        piece = self.__get_tile(x, y)
        for i, p in enumerate(self.pieces[piece.player]):
            if p.id == piece.id:
                del self.pieces[piece.player][i]
                return
            

    def __tile_on_board(self, x, y):
        if x < 0 or self.size <= x:
            return False
        if y < 0 or self.size <= y:
            return False
        return True   

    def __str__(self):
        string = "    %s\n" % "  ".join([chr(ord('a') + i) for i in range(self.size)])
        for y in range(self.size):
            string += "%d:  %s\n" % (y, " ".join(["--" if tile==None else str(tile) for tile in self.tiles[y]]))
        for player in [0, 1]:
            for piece in self.pieces[player]:
                string += "%s " % piece
            string += "\n"
        return string