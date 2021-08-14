
class Piece:

    def __init__(self, x, y, pieceStr, points, player):
        self.x = x
        self.y = y
        self.pieceStr = pieceStr
        self.points = points
        self.player = player

    def __str__(self):
        return self.pieceStr + self.player