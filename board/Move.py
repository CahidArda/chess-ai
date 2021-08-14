
class Move:

    def __init__(self, x1, y1, x2, y2, removed_piece = None):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.removed_piece = removed_piece

    def __str__(self):
        return f"Move from ({self.x1}, {self.y1}) to ({self.x2}, {self.y2})"