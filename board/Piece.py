
class Piece:

    def __init__(self, pieceStr, points, player):
        self.pieceStr = pieceStr
        self.points = points
        self.player = player

    def copy(self):
        return Piece(self.pieceStr, self.points, self.player)

    def __str__(self):
        return self.pieceStr + self.player