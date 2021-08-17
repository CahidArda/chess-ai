
class Move:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.removed_piece = None

    def __str__(self):
        to_column = lambda index: chr(97 + index)
        to_row    = lambda index: 8 - index
        return f"{to_column(self.x1)}{to_row(self.y1)}-{to_column(self.x2)}{to_row(self.y2)}"