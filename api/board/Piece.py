
count = 0

class Piece:

    def __init__(self, piece_str, points, player, x, y):
        self.piece_str = piece_str
        self.points = points
        self.player = player
        self.move_to(x,y)

        global count
        self.id = count
        count += 1

    def move_to(self,x,y):
        self.x = x
        self.y = y

    def mirrored_copy(self, board_size):
        copy = self.copy()
        copy.player = 1 - self.player
        copy.y = board_size - self.y - 1
        return copy

    def copy(self):
        return Piece(self.piece_str, self.points, self.player, self.x, self.y)

    def __str__(self):
        return self.piece_str + str(self.player)