
class Piece:

    def __init__(self, piece_str, points, player):
        self.piece_str = piece_str
        self.points = points
        self.player = player
        self.moved_before = False

    def copy(self):
        return Piece(self.piece_str, self.points, self.player)

    def __str__(self):
        return self.piece_str + self.player